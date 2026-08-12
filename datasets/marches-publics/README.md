---
license: cc0-1.0
language:
  - fr
pretty_name: marches-publics
tags:
  - public-procurement
  - boamp
  - france
---

# 📄 marches-publics — Corpus appels d'offres publics

Dataset cible : les avis de marchés publics (BOAMP / TED / profils d'acheteurs)
collectés et enrichis par le pipeline d'**AutoAO**.

> ⚠️ **État : squelette** — les données réelles sont collectées par le pipeline
> AutoAO (repo `autoao-saas`). Ce dossier définit le **contrat de données** pour
> que tout le portefeuille puisse consommer le corpus.

## Contrat de données (schéma cible)

```jsonc
// un objet par avis de marché
{
  "id": "hash-unique",
  "source": "boamp|ted|profil-acheteur",
  "source_id": "BOAMP-2426123",
  "published_at": "2026-08-12",
  "deadline": "2026-09-15",
  "autorite": "Mairie de X",
  "objet": "Fourniture de mobilier ergonomique",
  "categorie": "fournitures|services|travaux",
  "cpv": ["39100000-3"],
  "valeur_estimee_eur": 45000,
  "procedures": ["ouverte", "adaptée"],
  "criteria": ["prix 60%", "valeur technique 40%"],
  "documents": ["https://.../dce.pdf"],
  "enriched": {
    "resume_ia": "...",
    "score_fit_client": 0.82,
    "points_cles": ["...", "..."]
  }
}
```

## Pipeline cible

```
Collecte (BOAMP API / scraping) → Normalisation → Enrichissement IA (llm-gateway)
→ Publication dataset → RAG AutoAO (proposition de réponse) → CRM
```

## Fichiers

- `schema.json` — JSON Schema du contrat ci-dessus (à générer avec AutoAO)
- `avis/` — données collectées (à venir)
