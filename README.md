# 🌐 titoune33 AI Ecosystem

> **Un portefeuille de produits, de contenus et de données publiques, fédéré en un écosystème IA cohérent.**

Ce dépôt est le **cerveau du portefeuille** : il cartographie chaque projet, documente l'architecture cible, partage les briques réutilisables et publie les datasets construits à partir des données publiques du fondateur.

---

## 🗺️ La carte en une image

```
                    ┌─────────────────────────────────────────────┐
                    │          LLM GATEWAY (brique partagée)      │
                    │   DeepSeek · Mistral · Nemotron · local     │
                    └──────────────┬──────────────────────────────┘
                                   │
   ┌──────────────┬────────────────┼────────────────┬─────────────────┐
   │              │                │                │                 │
   ▼              ▼                ▼                ▼                 ▼
 RH &           MARCHÉS          NICHE           AGENTS /          DATA /
 CONFORMITÉ      PUBLICS          SEO             OUTILS            CONTENU
 ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐  ┌────────────┐
 │ Libera RH  │ │  AutoAO    │ │ BureauErgo │ │ Murmure    │  │ Datasets   │
 │ (égalité   │ │ (réponses  │ │ (affiliation│ │ (journal   │  │ benchmarks │
 │  salariale)│ │  AO IA)    │ │  +scraping)│ │  vocal)    │  │ corpus DRH │
 │ PeoplePulse│ │            │ │ Simulateur │ │ agentic-   │  │ marches    │
 │ (attrition)│ │            │ │ financier  │ │ inbox      │  │ publics    │
 │ TalentPulse│ │            │ │ extensions │ │ last30days │  │ pentest    │
 └────────────┘ └────────────┘ └────────────┘ └────────────┘  └────────────┘
```

## 🎯 La thèse

1. **Un marché, pas dix** : le vrai actif est le cluster **RH & conformité** (Libera RH, PeoplePulse, TalentPulse, guides DRH, analyse concurrentielle) — tous les autres projets sont soit des composants, soit des terrains d'essai.
2. **Une seule couche IA** : un `llm-gateway` partagé (routage, fallback, coûts, cache) évite de réimplémenter l'intégration DeepSeek/Mistral dans chaque SaaS.
3. **La donnée est un produit** : les guides, benchmarks et analyses sont transformés en **datasets publics** (voir [`datasets/`](datasets/)) qui nourrissent le RAG des produits et crédibilisent la marque.
4. **Zéro doublon** : consolidation des repos morts (`talent-pulse-`, `bureauergo`/`nichesite`…).

## 📦 Contenu du dépôt

| Chemin | Rôle |
|---|---|
| [`INVENTAIRE.md`](INVENTAIRE.md) | Reverse-engineering complet : tous les projets, stacks, statuts, doublons |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Architecture cible : briques partagées et flux de données |
| [`ROADMAP.md`](ROADMAP.md) | Plan d'optimisation par phases |
| [`datasets/`](datasets/) | Données publiques → datasets structurés (benchmarks LLM, corpus DRH, marchés publics) |
| [`packages/`](packages/) | Specs des briques partagées (llm-gateway, auth-billing, scraper, export) |
| [`scripts/`](scripts/) | Générateurs de datasets |

## 🚀 Démarrage rapide

```bash
# Reconstruire tous les datasets depuis les sources
python3 scripts/build_datasets.py
```

## 📜 Licence

Contenu du fondateur © 2026 titoune33 — sauf mention contraire dans chaque dataset (sources publiques citées pour les benchmarks).
