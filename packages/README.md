# 📦 packages — Briques partagées

> Les composants réutilisables que chaque produit du portefeuille doit consommer.
> Statut actuel : **specs** (Phase 3 de la roadmap pour l'implémentation).

| Package | Rôle | Consommateurs |
|---|---|---|
| [`llm-gateway/`](llm-gateway/) | Intégration LLM unifiée : routage, fallback, coûts, cache, RAG | Tous les SaaS IA |
| [`auth-billing/`](auth-billing/) | Auth (cookie/session) + Stripe, partagés depuis Libera RH/saaskit | SaaS payants |
| [`scraper/`](scraper/) | Collecte : produits (niches), marchés publics (AutoAO), web | BureauErgo, AutoAO |
| [`export/`](export/) | Génération docx/xlsx/pdf (déjà utilisé dans Libera RH) | Libera RH, rapports |

## Principes

1. Chaque package est **indépendant et testable** (pas de couplage entre briques).
2. Versionnage sémantique ; publié en npm scoped `@titoune33/*` ou copié dans `saaskit`.
3. Le `llm-gateway` est la seule brique qui parle aux providers LLM.
