# 🛣️ Roadmap d'optimisation

> Priorisé par impact / effort. Chaque phase est indépendante.

## Phase 1 — Nettoyage & fondations (fait dans ce dépôt ✅)

- [x] Cartographie complète du portefeuille (`INVENTAIRE.md`)
- [x] Architecture cible et briques partagées (`ARCHITECTURE.md`)
- [x] Datasets publiés : benchmarks LLM, corpus DRH, squelette marchés publics
- [x] Specs des packages partagés
- [x] Nettoyage GitHub : descriptions, archive de `talent-pulse-`

## Phase 2 — Consolidation RH (le cœur du portefeuille)

- [ ] **Fusionner Libera RH + PeoplePulse + TalentPulse en une plateforme** : un seul repo public `libera-rh` (conformité salariale) + module analytics (attrition) — même auth, même billing (saaskit), même llm-gateway
- [ ] Rendre public `equilibre-transparence-salariale` (→ `libera-rh`) après vérification des secrets
- [ ] Fusionner `bureauergo`/`nichesite` et `agrinorm` ×3

## Phase 3 — Industrialiser la couche IA

- [ ] Implémenter `packages/llm-gateway` (TypeScript, d'abord dans le monorepo `saaskit`)
- [ ] Brancher le RAG `drh-conformite` dans le copilote Libera RH
- [ ] Publier les datasets sur HuggingFace (`titoune33/benchmarks-llm`, `titoune33/drh-conformite`)
- [ ] Dashboard usage/coût LLM par produit

## Phase 4 — Monétiser la donnée

- [ ] Corpus marchés publics : pipeline de collecte BOAMP (autoao) → dataset
- [ ] Dataset pentest anonymisé → contenu blog/branding sécurité
- [ ] Guides DRH → lead magnets + RAG public (portail)

## Phase 5 — Vitrine

- [ ] Landing `ecosystem` : un site qui liste les produits + datasets (le README devient une page)
- [ ] Badges GitHub cohérents, README de chaque produit
- [ ] Intégration continue : tests datasets (schéma), CI sur chaque repo

## KPI de succès

| Métrique | Aujourd'hui | Cible 90 jours |
|---|---|---|
| Repos actifs (non-doublons) | ~5 utiles / 7 | 6, tous documentés |
| Intégrations LLM distinctes | ~4 ad hoc | 1 (llm-gateway) |
| Datasets publics | 0 | 3-4 |
| Produits utilisant le RAG DRH | 0 | 2 |
