# scraper — Spec

Collecte de données externes. Déjà expérimentée dans bureauergo (scraping
produits d'affiliation) et autoao (marchés publics).

## Modes

| Mode | Usage | Exemple |
|---|---|---|
| `products` | Prix/fiches produits e-commerce | bureauergo (affiliation) |
| `ao` | Avis de marchés publics (BOAMP/TED) | AutoAO |
| `web` | Pages génériques (contenu, contact) | enrichissement niche |

## API cible

```ts
import { scrape } from "@titouane33/scraper";

const items = await scrape.products({ urls: [...], fields: ["title", "price", "image"] });
const avis = await scrape.ao({ query: "mobilier ergonomique", since: "2026-08-01" });
```

## Exigences

- Respect des `robots.txt` et des CGU des sites source (collecte légale).
- Rate limiting + retry exponentiel + rotation d'UA.
- Sortie normalisée → mêmes schémas que `datasets/marches-publics/schema.json`.
- Dédoublonnage par hash de contenu.
