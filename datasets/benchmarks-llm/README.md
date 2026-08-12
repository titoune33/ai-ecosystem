---
license: cc-by-4.0
language:
  - fr
  - en
pretty_name: benchmarks-llm
tags:
  - llm
  - benchmarks
  - artificial-analysis
  - deepseek
  - mistral
  - nvidia-nemotron
  - xiaomi-mimo
  - model-routing
---

# 🤖 benchmarks-llm

Comparaisons de modèles LLM établies à partir de sources publiques (Artificial Analysis, BenchLM, Vals.ai, NVIDIA, OpenRouter, docs officielles) et des rapports internes titoune33 (11-12/08/2026).

## Fichiers

| Fichier | Contenu |
|---|---|
| `models.json` | Fiches structurées : 6 modèles (DeepSeek V4 Flash 0731, Mistral Large 3, Mistral Medium 3.5, Mistral Small 4, Nemotron 3.5 Lightning, MiMo V2.5) |
| `comparisons.jsonl` | 14 comparaisons chiffrées pairwise (1 ligne = 1 métrique × 2 modèles) |

## Schéma `models.json`

```jsonc
{
  "id": "slug-unique",
  "vendor": "éditeur",
  "release_date": "ISO-8601 ou null",
  "architecture": "MoE | null",
  "params_total_b": 284,        // milliards, total
  "params_active_b": 13,        // milliards, actifs
  "context_tokens": 1000000,
  "input_image": true|false,    // + input_video, input_audio, reasoning
  "open_weights": true|false,
  "license": "MIT | proprietary | modified-open",
  "price_input_usd_per_mtok": 0.14,   // USD par M tokens
  "price_output_usd_per_mtok": 0.28,
  "price_cache_hit_usd_per_mtok": 0.0028,
  "intelligence_aa_index": 52,        // Artificial Analysis Intelligence Index v4.1.1
  "speed_output_tok_per_s": 131,
  "time_to_first_token_s": 1.44,
  "agent_benchmarks": { "terminal_bench_2_1": 82.7, ... },
  "benchlm_public_score": null,
  "notes": "..."
}
```

## Schéma `comparisons.jsonl`

```jsonc
{
  "comparison": "slug-a_vs_slug-b",
  "date": "2026-08-11",
  "metric": "intelligence_aa_index",   // clé du modèle ou nom libre
  "values": { "slug-a": 52, "slug-b": 30 },
  "winner": "slug-a" | null,           // null si égalité/non comparable
  "note": "optionnel",
  "source": "Artificial Analysis"
}
```

## Licence & sources

- Données factuelles : **CC BY 4.0** — sources citées dans `models.json` (urls) et dans les rapports d'origine.
- Rapports internes titoune33 (benchmark DeepSeek vs Mistral, 11/08 ; MiMo vs DeepSeek, 12/08) : © titoune33.

## Usage

- **Routage de modèles** : entrée du `llm-gateway` (choisir le modèle par tâche, coût et vitesse).
- **Décisions d'achat** : DeepSeek-V4-Flash-0731 = meilleur rapport intelligence/prix pour texte/agent ; MiMo V2.5 = multimodal ; Nemotron = exécution locale.
