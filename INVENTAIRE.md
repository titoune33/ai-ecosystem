# 📋 Inventaire du portefeuille — Reverse-engineering

> Établi le 12/08/2026. Source : compte GitHub `titoune33`, dossiers locaux, déploiements Vercel.
> Légende : 🟢 actif · 🟡 dormant · 🔴 doublon/dette · ⚪ placeholder

## 1. Repos GitHub (7)

| Repo | Visibilité | Stack | Statut | Produit / rôle |
|---|---|---|---|---|
| `libera-rh` (ex-`equilibre-transparence-salariale`) | **public** ✅ | React+Vite, API Vercel, Airtable, Stripe, **llm-gateway** | 🟢 | **LA plateforme RH** : conformité salariale (Egapro, UE 2023/970) + benchmark + **module attrition** (ex-TalentPulse/PeoplePulse) — [libera-rh.vercel.app](https://libera-rh.vercel.app) |
| `murmure` | public | HTML, Express+SQLite | 🟢 | Journal vocal one-page — [murmure-rho.vercel.app](https://murmure-rho.vercel.app) |
| `peoplepulse-hr-saas` | public | Next.js, Prisma, libsql | 🟡 | **Absorbé par libera-rh** (module attrition) — gardé comme référence |
| `autoao-saas` | public | TypeScript (Next.js) | 🟢 | **AutoAO** — réponses IA aux appels d'offres publics |
| `TalentPulse` | public | FastAPI (Python) + Airtable | 🟡 | **Absorbé par libera-rh** (scoring porté en TS) — gardé comme référence |
| `talent-pulse-` | public | — | 🔴 | **Archivé** (coquille vide) |
| `mistral` | privé | JavaScript | 🟡 | Expérimentations « pour tout faire » |

## 2. Projets locaux (~/Projects, ~/tout mes saas créées)

### SaaS produits
| Projet | Stack | Statut | Note |
|---|---|---|---|
| `libera-rh` (dans « tout mes saas créées ») | React+Vite, API Vercel | 🟢 | Version landing+app du SaaS RH (voir repo privé) |
| `plombio` (dans « tout mes saas créées ») | Express, SQLite | 🟡 | Gestion plomberie : devis, factures — `seed.js` + `data/` |
| `Equitia-saas-rh.tar.gz` (dans « tout mes saas créées ») | — | 🟡 | Archive de l'app Équitia (ancêtre de Libera RH) |
| `agrinorm` / `agrinorm-mvp` / `agrinorm-final` | Next.js, Firebase | 🟡 | SaaS agritech — 3 versions = dette à consolider |
| `autoao` (local) | Next.js | 🟢 | Version locale d'AutoAO |
| `peoplepulse` (local) | Next.js, Prisma, libsql | 🟢 | Version locale de PeoplePulse |
| `nexus` | React+Vite / Express+SQLite+JWT+WS | 🟡 | SaaS project management |
| `saaskit` | Next.js, Prisma, NextAuth, Stripe | 🟢 | **Starter kit SaaS** — la base commune de tous les SaaS |
| `failles` (dans « tout mes saas créées ») | React+Vite, API Vercel, JSON sourcé | 🟢 | **Failles** — « Le Shodan des failles capitalistes » : aides oubliées & optimisations légales — [failles.vercel.app](https://failles.vercel.app) (repo GitHub : à créer) |
| `mon-api-vercel` | — | 🟡 | Mini-API de test Vercel |

### Sites de niche / SEO monétisés
| Projet | Stack | Statut | Note |
|---|---|---|---|
| `bureauergo` (= `nichesite`) | — | 🔴 | **Doublon** : mêmes fichiers, niche « accessoires bureau ergonomiques », scraping + affiliation |
| `ergoconfort` | HTML statique | 🟡 | Landing même niche |
| `simulateur-financier` | HTML/JS statique | 🟡 | Blog + simulateur |

### Extensions / outils
| Projet | Stack | Statut | Note |
|---|---|---|---|
| `email-signature-parser` | Chrome extension | 🟡 | Parser de signatures email |
| `smart-form-filler` | Chrome extension | 🟡 | Auto-remplissage de formulaires |
| `finsep-terminal` | — | 🟡 | Fork Fincept Terminal (finance) — upstream en maintenance |
| `openllmvtube` | — | 🟡 | Fork Open-LLM-VTuber (avatar IA parlant) |
| `odysseus` | Anthropic SDK | 🟡 | Agent expérimental |
| `agentic-inbox` (= `adjantic-inbox`) | Cloudflare, AI chat | 🟡 | Inbox agentique |
| `black-cat-pub` | — | 🟡 | Contenus email marketing |
| `last30days-skill` | Python skill package | 🟢 | Fork du skill de recherche multi-sources (Reddit/X/YT/web) — **installable partout** |

### Infra / forks (outillage)
`bolt.diy`, `librechat`, `agent-zero`, `openclaw`, `firecrawl`, `bugbounty-kit`, `hyperframe`, `kimi`, `mcp-ical`, `mail-mcp`, `go`, `Code`, `GitHub` (dossiers de travail)

## 3. Données publiques & contenu (~/freebuf)

| Fichier | Contenu | Exploitation |
|---|---|---|
| `BENCHMARK-DEEPSEEK-V4-FLASH-VS-MISTRAL.md` | Benchmark LLM cité (Artificial Analysis, BenchLM) + décision | → `datasets/benchmarks-llm/` |
| `Benchmark-MiMo-V2-5-vs-DeepSeek-V4-Flash-0731.pdf` | Benchmark PDF | → `datasets/benchmarks-llm/` |
| `GUIDE-CHATGPT-BUSINESS-DRH*.md/.pdf` | Guides DRH (2 pages + complet) | → `datasets/drh-conformite/` (corpus RAG) |
| `ANALYSE-CONCURRENTIELLE.md` | Marché conformité salariale FR/UE | → `datasets/drh-conformite/` |
| `CAMPAGNE-MARKETING.md` + `skills/marketing-campaign/` | Campagne marketing Libera RH | → README du corpus |
| `docs/positionnement.md` | Positionnement produit | → README du corpus |
| `~/Downloads/pentest frebuf/`, `~/pentest/`, `~/open code pentest/` | Rapports de pentest (keycloak, exodus, chia, chainlink…) | → `datasets/pentest/` (index anonymisé) |

## 4. Synthèse : les 5 clusters

1. **RH & conformité (le cœur)** : Libera RH + PeoplePulse + TalentPulse + guides/analyses DRH → **une plateforme RH, deux modules**.
2. **Marchés publics** : AutoAO (+ plombio comme terrain d'essai devis/factures).
3. **Niche SEO** : BureauErgo, simulateur-financier → usine à sites.
4. **Outillage IA** : saaskit, llm-gateway (à créer), last30days, agentic-inbox, datasets.
5. **Failles / optimisation financière légale** : Failles (aides non réclamées, crédits d'impôt, droits) + bot scanner → dataset `aides-non-requises` réutilisable (RAG, contenu SEO).

## 5. Dette technique détectée

| Dette | Action |
|---|---|
| `talent-pulse-` (repo vide) vs `TalentPulse` vs `peoplepulse-hr-saas` | Archiver `talent-pulse-` ; décider du nom de famille (PeoplePulse) |
| `bureauergo` == `nichesite` | Fusionner, garder un seul |
| `agrinorm` × 3 versions | Consolider en un repo |
| `equilibre-transparence-salariale` (privé) vs `libera-rh` local vs `freebuf` (dossier) | Un seul nom : **Libera RH** ; un seul repo (le rendre public) |
| `adjantic-inbox` vs `agentic-inbox` | Renommer proprement |
| Naming chaotique (espaces, accents, « frebuf ») | Normaliser les noms de dossiers locaux |
