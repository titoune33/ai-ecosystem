# 📊 Datasets publics

> Les données publiques du portefeuille, transformées en datasets structurés et réutilisables (RAG, benchmarks, choix de modèles).

## Catalogue

| Dataset | Contenu | Format | Consommateurs |
|---|---|---|---|
| [`benchmarks-llm/`](benchmarks-llm/) | Fiches modèles + comparaisons chiffrées (DeepSeek V4 Flash 0731, Mistral Large 3 / Medium 3.5, Nemotron 3.5 Lightning, MiMo V2.5) | JSON + JSONL | `llm-gateway` (routage), décisions d'achat |
| [`drh-conformite/`](drh-conformite/) | Corpus RAG : guides DRH, analyse concurrentielle, positionnement | Markdown + manifest | Copilote Libera RH, PeoplePulse, portail |
| [`marches-publics/`](marches-publics/) | Squelette : schéma + pipeline de collecte (source : AutoAO / BOAMP) | JSON Schema + README | AutoAO |

## Règles

1. Chaque dataset a un `README.md` : schéma, licence, sources citées, date de mise à jour.
2. Les données sont **reproductibles** : `python3 scripts/build_datasets.py` régénère/valide tout depuis les sources.
3. Licence par défaut : **CC BY 4.0** pour les données factuelles issues de sources publiques ; contenu éditorial du fondateur © titoune33 (voir chaque README).

## Publication cible

- HuggingFace Hub : `titoune33/benchmarks-llm`, `titoune33/drh-conformite`, `titoune33/marches-publics`
- Ce repo GitHub public sert de source de vérité.
