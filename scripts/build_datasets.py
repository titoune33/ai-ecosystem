#!/usr/bin/env python3
"""Build/validate les datasets de l'écosystème.

Usage :
    python3 scripts/build_datasets.py

Ce script est la source de vérité de la construction des datasets :
- valide benchmarks-llm (models.json + comparisons.jsonl)
- copie le corpus DRH depuis ~/freebuf (sources) vers datasets/drh-conformite/
- génère le manifest du corpus DRH
"""
from __future__ import annotations

import json
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASETS = ROOT / "datasets"

# Sources locales du corpus DRH (ordre = priorité de lecture)
DRH_SOURCES = [
    ("/Users/titouanwajda/freebuf/GUIDE-CHATGPT-BUSINESS-DRH-COMPLET.md",
     "guide-chatgpt-business-drh-complet.md", "Guide ChatGPT Business DRH (complet)"),
    ("/Users/titouanwajda/freebuf/GUIDE-CHATGPT-BUSINESS-DRH.md",
     "guide-chatgpt-business-drh-2pages.md", "Guide ChatGPT Business DRH (2 pages)"),
    ("/Users/titouanwajda/freebuf/ANALYSE-CONCURRENTIELLE.md",
     "analyse-concurrentielle-equitia.md", "Analyse concurrentielle — marché conformité salariale"),
    ("/Users/titouanwajda/freebuf/docs/positionnement.md",
     "positionnement-libera-rh.md", "Positionnement produit Libera RH"),
    ("/Users/titouanwajda/freebuf/CAMPAGNE-MARKETING.md",
     "campagne-marketing-libera-rh.md", "Campagne marketing Libera RH"),
]


def validate_benchmarks() -> None:
    bdir = DATASETS / "benchmarks-llm"
    with open(bdir / "models.json", encoding="utf-8") as fh:
        data = json.load(fh)
    models = {m["id"] for m in data["models"]}
    assert "deepseek-v4-flash-0731" in models, "modèle de référence manquant"

    with open(bdir / "comparisons.jsonl", encoding="utf-8") as fh:
        rows = [json.loads(line) for line in fh if line.strip()]
    for row in rows:
        for sid in row["values"]:
            assert sid in models, f"{sid} référencé dans comparisons.jsonl mais absent de models.json"
    print(f"✓ benchmarks-llm : {len(models)} modèles, {len(rows)} comparaisons")


def build_drh_corpus() -> None:
    target = DATASETS / "drh-conformite"
    target.mkdir(parents=True, exist_ok=True)
    manifest = []
    for src, dest_name, title in DRH_SOURCES:
        src_path = Path(src)
        if not src_path.exists():
            print(f"⚠ source absente : {src_path}")
            continue
        dest = target / dest_name
        # normalise : pas de BOM, fin de ligne unix
        content = src_path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
        dest.write_text(content, encoding="utf-8")
        manifest.append({
            "file": dest_name,
            "title": title,
            "source": str(src_path),
            "bytes": dest.stat().st_size,
        })
    manifest_path = target / "manifest.json"
    manifest_path.write_text(
        json.dumps({"generated": date.today().isoformat(), "files": manifest},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✓ drh-conformite : {len(manifest)} fichiers copiés + manifest")


def main() -> None:
    validate_benchmarks()
    build_drh_corpus()
    print("✓ datasets OK")


if __name__ == "__main__":
    sys.exit(main())
