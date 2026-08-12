# Dataset `aides-non-requises` — aides oubliées & optimisations légales (France)

> Corpus curé des dispositifs publics méconnus et des optimisations légales
> pour particuliers et PME. Alimente le produit **Failles**
> (failles.vercel.app) et est réutilisable en RAG / contenu SEO.

## Statut

- 🟢 **v1 publiée** le 12/08/2026 — 44 entrées sourcées (barèmes 2026).
- Source canonique : `data/aides.json` dans le repo du produit Failles
  (dossier « tout mes saas créées »/failles).
- Le bot `scripts/scanner.py` (data.gouv.fr, aides-territoires) produit des
  candidats à intégrer dans `data/candidats/<date>.json`.

## Schéma d'une entrée

```json
{
  "id": "cheque-energie",
  "titre": "Chèque énergie",
  "type": "aide",                 // aide | credit_impot | exoneration | droit | pret | negociation | arbitrage | epargne
  "categorie": "energie",         // energie | logement | famille | travail | entreprise | impots | epargne | consommation | mobilite | culture | sante | local
  "montant": { "min": 48, "max": 277, "unite": "€/an" },
  "effort": "faible",             // faible | moyen | eleve
  "fiabilite": "officiel",        // officiel | commun
  "maj": "2026-08",               // date de vérification des barèmes
  "desc": "…",
  "conditions_texte": ["…"],
  "conditions": { "rfr_uc_max": 11000 },   // prédicats machine (moteur de matching)
  "sources": [{ "nom": "service-public.gouv.fr", "url": "https://…" }],
  "demarches": "…"
}
```

## Prédicats du moteur

`toujours`, `rfr_uc_max`, `revenu_max/min`, `ars_plafond`, `statut_in/not_in`,
`salarie`, `demandeur_emploi`, `etudiant`, `micro`, `occupation_in`,
`construction_in`, `chauffage_in`, `logement_neuf`, `travaux_energie`,
`grande_renovation`, `achat_residence`, `pret_immo_encours`,
`transports_publics`, `voiture`, `velo_souhaite`, `services_domicile`,
`garde_enfants`, `boursier`, `enfant_handicap`, `enfants_min`,
`enfants_0_5_min`, `enfants_6_18_min`, `entreprise_actif`,
`entreprise_effectifs_max`, `entreprise_age_max_mois`, `entreprise_rd`,
`embauche_prevue`, et le combinatoire `ou` (branches en ET).

## Règles de curation (non négociables)

1. Au moins une source officielle accessible par entrée.
2. Montants = barèmes en vigueur à la date `maj` ; doute → fourchette + lien.
3. Zéro fraude, zéro évasion : uniquement des dispositifs légaux.

## Sources primaires

- service-public.gouv.fr / entreprendre.service-public.gouv.fr
- economie.gouv.fr, caf.fr, urssaf.fr, ameli.fr
- france-renov.gouv.fr, maprimerenov.gouv.fr, pass.sports.gouv.fr
- API data.gouv.fr (datasets « aides »), API aides-territoires (token requis)

## Licence

Annotations & curation : **CC BY-SA 4.0**. Données sources : éditeurs respectifs.
