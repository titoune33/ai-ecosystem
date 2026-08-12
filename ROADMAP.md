# 🛣️ Roadmap d'optimisation

> Priorisé par impact / effort. Chaque phase est indépendante.

## Phase 1 — Nettoyage & fondations (fait ✅)

- [x] Cartographie complète du portefeuille (`INVENTAIRE.md`)
- [x] Architecture cible et briques partagées (`ARCHITECTURE.md`)
- [x] Datasets publiés : benchmarks LLM, corpus DRH, squelette marchés publics
- [x] Specs des packages partagés
- [x] Nettoyage GitHub : descriptions, archive de `talent-pulse-`

## Phase 2 — Consolidation RH (fait ✅)

- [x] **Libera RH devient LA plateforme** : repo public `libera-rh` (ex-`equilibre-transparence-salariale`)
- [x] Module **attrition** intégré (ex-TalentPulse/PeoplePulse) : scoring déterministe porté en TS, page « Risque de départ », endpoint `/api/attrition`
- [x] Vérification secrets avant passage public (aucun `.env` suivi, audit `git grep`)
- [x] `talent-pulse-` archivé ; `TalentPulse` + `peoplepulse-hr-saas` marqués « absorbés »

## Phase 3 — Industrialiser la couche IA (fait ✅)

- [x] **`llm-gateway` implémenté** (`packages/llm-gateway` dans libera-rh) : routage par tâche (DeepSeek/Qwen/MiMo/Nemotron/Mistral), fallback auto, budget, cache 10 min, coûts — 12 tests unitaires + smoke test réel conditionnel
- [x] `api/assistant.ts` refactorisé sur le gateway (contrat frontend inchangé)
- [x] Datasets publiés sur HuggingFace (`titoune33/benchmarks-llm`, `titoune33/drh-conformite`)
- [ ] Dashboard usage/coût LLM par produit (reste : UI simple sur le compteur du gateway)

## Phase 4 — Monétiser la donnée

- [ ] Corpus marchés publics : pipeline de collecte BOAMP (autoao) → dataset
- [ ] Dataset aides non réclamées (`aides-non-requises`) : base sourcée de Failles + candidats du scanner → RAG produit + contenu SEO
- [ ] Brancher Stripe sur Failles (plan Premium 9 €/mois) + cron hebdo du scanner
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
