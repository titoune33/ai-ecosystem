# llm-gateway — Spec

Intégration LLM unifiée du portefeuille.

## API cible

```ts
import { llm } from "@titouane33/llm-gateway";

const res = await llm.complete({
  prompt: string,
  system?: string,
  model?: "auto" | ModelId,       // "auto" = routage
  maxCostUsd?: number,             // budget par appel
  corpus?: "drh-conformite" | "marches-publics",  // RAG optionnel
  json?: boolean,                  // sortie JSON contrainte
});

// → { text, model, costUsd, tokensIn, tokensOut, latencyMs, cached }
```

## Routage par défaut (`model: "auto"`)

| Tâche | Modèle | Justification (datasets/benchmarks-llm) |
|---|---|---|
| Raisonnement / agent / codage | `deepseek-v4-flash-0731` | AA index 52, Terminal-Bench 82.7, 1M ctx, 0.14$/0.28$ |
| Exécution à haut volume (tests, refactors) | `nemotron-3.5-lightning` (local si dispo) | 24 AA, 3B actifs, local, ~0.05$/0.20$ |
| Multimodal (images, slides) | `mimo-v2-5` | Natif texte/image/vidéo/audio, MIT |
| Prose française premium | `mistral-medium-3-5` (optionnel) | Réputation rédactionnelle FR, 30 AA |

## Exigences

- **Fallback** : si le provider principal échoue → second choix configuré, jamais d'erreur visible.
- **Coûts** : log par produit (dashboard), budget max par appel et par jour.
- **Cache** : prompts identiques (hash) → réponse en cache (économie majeure : cache hit 0.0028$/M chez DeepSeek).
- **Clés** : dans `~/.hermes/.env` / `.env.local`, jamais dans les repos.
- **Tests** : mock provider, assertions de routage et de budget.

## Implémentation

- Langage : TypeScript (toute la stack produit est TS/Next.js).
- Hébergement : fonctions Vercel (comme l'API actuelle de Libera RH).
- Sources de données : `datasets/benchmarks-llm/models.json` pour la table de routage.
