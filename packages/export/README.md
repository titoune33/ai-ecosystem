# export — Spec

Génération de documents. Déjà utilisée dans Libera RH (deps `docx`, `xlsx`).

## API cible

```ts
import { exportDoc } from "@titouane33/export";

await exportDoc.docx({ template: "rapport-egalite", data: {...} });  // → Blob
await exportDoc.xlsx({ sheets: [{ name, rows }] });                  // → Blob
await exportDoc.pdf({ html });                                       // → Blob
```

## Cas d'usage

- Libera RH : rapport d'égalité salariale (docx), export benchmark (xlsx), CGV (pdf).
- PeoplePulse : rapports d'attrition.
- AutoAO : mémoire technique (docx) en réponse aux AO.

## Exigences

- Templates versionnés (dossier `templates/`), données injectées sans logique
  de présentation dans le code produit.
- Tests golden : un docx/xlsx généré est comparé octet à octet à une référence.
