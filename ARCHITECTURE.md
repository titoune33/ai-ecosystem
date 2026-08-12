# 🏗️ Architecture cible de l'écosystème IA

## Principes

1. **Un noyau, des produits** : tout SaaS partage les mêmes briques (auth, billing, LLM, export). Un changement de modèle de coût ou de provider se propage partout.
2. **La donnée au centre** : les datasets publics alimentent le RAG des produits et sont réutilisables entre eux (corpus DRH → copilote Libera RH **et** PeoplePulse).
3. **Tout est déployable indépendamment** : chaque produit garde son repo, le hub `ai-ecosystem` référence et spécifie, sans monolithe.

## Couches

```
┌─────────────────────────────────────────────────────────────┐
│  PRODUITS (repos indépendants)                              │
│  libera-rh · peoplepulse · autoao · plombio · murmure ·     │
│  nichesite · extensions · agentic-inbox                     │
└───────────────┬───────────────────────────┬─────────────────┘
                │ consomme                  │ publie
┌───────────────▼──────────────────┐  ┌─────▼──────────────────┐
│  BRIQUES PARTAGÉES (packages/)   │  │  DONNÉES (datasets/)   │
│  llm-gateway  → routage/fallback │  │  benchmarks-llm        │
│  auth-billing → cookie/Stripe    │  │  drh-conformite (RAG)  │
│  scraper      → produits/AO/SEO  │  │  marches-publics       │
│  export       → docx/xlsx/pdf    │  │  pentest (index)       │
│  saaskit      → starter Next.js  │  │                        │
└───────────────┬──────────────────┘  └───────────┬────────────┘
                │                                 │ ingestion
┌───────────────▼──────────────────────────────────▼───────────┐
│  INFRA (déjà en place)                                       │
│  Vercel (apps + API) · Airtable · SQLite/libsql · Stripe ·   │
│  GitHub (gh, MCP) · Hermes · ollama (local) · Cloudflare     │
└──────────────────────────────────────────────────────────────┘
```

## La brique critique : `llm-gateway`

Objectif : **une seule intégration LLM pour tout le portefeuille.**

```ts
// Usage cible (spec)
import { llm } from "@titoune33/llm-gateway";

const res = await llm.complete({
  prompt: "Rédige une fourchette salariale pour un poste X",
  model: "auto",            // routage : fort pour raisonner, léger pour exécuter
  maxCostUsd: 0.02,         // budget par appel
  context: { corpus: "drh-conformite" }, // RAG optionnel
});

// Comportements
- routage par tâche (raisonnement → DeepSeek-V4-Flash, exécution → Nemotron local, prose FR → Mistral)
- fallback automatique si provider down
- logging coût/usage par produit (→ dashboard)
- cache de prompts identiques
```

**Pourquoi c'est prioritaire** : chaque SaaS du portefeuille a déjà ou aura sa propre intégration LLM. Le benchmark `deepseek-vs-mistral` (voir `datasets/`) a déjà tranché le choix du modèle principal — il ne reste qu'à l'industrialiser.

## Flux de données cible

```
Sources (données publiques)           Datasets (publiés)          Produits (consommateurs)
────────────────────────────          ──────────────────          ────────────────────────
Benchmarks Artificial Analysis ──►    benchmarks-llm/        ──►  choix modèle llm-gateway
Guides DRH / analyse concurrentielle ► drh-conformite/       ──►  copilote Libera RH
BOAMP / AO publiques (autoao)    ──►  marches-publics/       ──►  AutoAO
Rapports pentest (anonymisés)    ──►  pentest/               ──►  bugbounty-kit, blog sécu
```

## Règles de gouvernance

- Un produit = un repo = un nom (pas de `talent-pulse-` + `TalentPulse` + `peoplepulse`).
- Toute nouvelle intégration LLM passe par `llm-gateway`.
- Tout dataset publié a : README, schéma, licence, sources citées.
- Les secrets restent dans `~/.hermes/.env` / `.env.local` — jamais dans les repos publics.
