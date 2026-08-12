# 📚 drh-conformite — Corpus RAG « RH & conformité »

Corpus documentaire du cluster RH (Libera RH / PeoplePulse), prêt pour le RAG
(embeddings + recherche vectorielle) et la génération augmentée.

## Contenu

| Fichier | Rôle RAG |
|---|---|
| `guide-chatgpt-business-drh-complet.md` | Méthodes : cloisonnement clients, capitalisation, briefs |
| `guide-chatgpt-business-drh-2pages.md` | Version condensée du guide |
| `analyse-concurrentielle-equitia.md` | Marché conformité salariale FR/UE, directive 2023/970, Egapro |
| `positionnement-libera-rh.md` | Message produit, cibles, différenciation |
| `campagne-marketing-libera-rh.md` | Arguments de vente, canaux, scripts |
| `manifest.json` | Généré par `scripts/build_datasets.py` (sources + tailles) |

## Usage typique (copilote)

```
Question : « Une PME de 80 salariés doit-elle publier des fourchettes salariales ? »
→ retrieval sur analyse-concurrentielle-equitia.md + positionnement-libera-rh.md
→ réponse sourcée + argumentaire de vente
```

## Schéma du manifest

```jsonc
{ "generated": "2026-08-12", "files": [ { "file": "...", "title": "...", "source": "chemin d'origine", "bytes": 1234 } ] }
```

## Licence

Contenu éditorial © titoune33. Libre d'utilisation dans les produits du portefeuille ;
publication externe soumise à l'accord du fondateur.
