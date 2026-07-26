#!/usr/bin/env python3
"""Run synomega locally and print JSON, loading the model + stock from env vars.

A thin convenience wrapper over the installed `synomega` package so an agent can
call any of the three operations uniformly (the package CLI has no single-step
subcommand). Requires: `pip install "synomega[gnn]"`.

Environment:
    SYNOMEGA_MODEL       trained run directory (contains best.pt + config.yaml)  [required]
    SYNOMEGA_STOCK       building-block file (.keys or raw .smi catalogue)       [required]
    SYNOMEGA_STOCK_KEYS  "1" if SYNOMEGA_STOCK is a precomputed .keys file       [default 0]
    SYNOMEGA_DEVICE      torch device, e.g. "cpu" or "cuda:0"                    [default cpu]

Usage:
    python synomega_run.py single-step "CC(=O)Nc1ccccc1O" --top-k 10
    python synomega_run.py plan        "CC(=O)Nc1ccccc1O" --max-depth 5 --algorithm retrostar
    python synomega_run.py score        "CC(=O)Nc1ccccc1O" --max-steps 5
"""
from __future__ import annotations

import argparse
import json
import os
import sys


def _truthy(name: str) -> bool:
    return os.environ.get(name, "").lower() in {"1", "true", "yes", "on"}


def _load(algorithm: str):
    """Build (model, planner). Uses SYNOMEGA_MODEL/SYNOMEGA_STOCK if set,
    otherwise downloads the default pretrained model + stock on first use."""
    try:
        from synomega import Planner
        from synomega.singlestep import TemplateGNN
        from synomega.stock import InMemoryStock
    except ImportError:
        sys.exit('synomega is not installed. Run:  pip install "synomega[gnn]"')

    device = os.environ.get("SYNOMEGA_DEVICE", "cpu")
    model_path = os.environ.get("SYNOMEGA_MODEL", "").strip()
    stock_path = os.environ.get("SYNOMEGA_STOCK", "").strip()

    # Model: explicit path, or the auto-downloaded default.
    if model_path:
        model = TemplateGNN.from_pretrained(model_path, device=device)
    else:
        model = TemplateGNN.default(device=device)

    # Stock: explicit path, or the auto-downloaded default.
    if stock_path:
        stock = (
            InMemoryStock.from_keys_file(stock_path)
            if _truthy("SYNOMEGA_STOCK_KEYS")
            else InMemoryStock.from_file(stock_path)
        )
    else:
        stock = InMemoryStock.default()

    planner = Planner(model, stock, algorithm=algorithm)
    return model, planner


def main() -> int:
    p = argparse.ArgumentParser(description="run synomega locally -> JSON")
    sub = p.add_subparsers(dest="cmd", required=True)

    ss = sub.add_parser("single-step")
    ss.add_argument("smiles")
    ss.add_argument("--top-k", type=int, default=20)

    pl = sub.add_parser("plan")
    pl.add_argument("smiles")
    pl.add_argument("--algorithm", default="retrostar",
                    choices=["retrostar", "mcts", "bfs"])
    pl.add_argument("--max-depth", type=int, default=5)
    pl.add_argument("--max-routes", type=int, default=5)
    pl.add_argument("--exclude-target", action="store_true",
                    help="treat the target as not purchasable even if it is in "
                         "the stock (avoids a trivial zero-step solution)")

    sc = sub.add_parser("score")
    sc.add_argument("smiles")
    sc.add_argument("--max-steps", type=int, default=5)
    sc.add_argument("--algorithm", default="retrostar",
                    choices=["retrostar", "mcts", "bfs"])
    sc.add_argument("--exclude-target", action="store_true",
                    help="treat the target as not purchasable even if it is in "
                         "the stock (avoids a trivial zero-step solution)")

    args = p.parse_args()

    if args.cmd == "single-step":
        model, _ = _load("retrostar")
        preds = model.predict(args.smiles, top_k=args.top_k)
        out = {
            "target": args.smiles,
            "predictions": [
                {
                    "rank": i,
                    "reactants": list(pred.reactants),
                    "score": round(float(pred.score), 6),
                    "template_id": pred.template_id,
                }
                for i, pred in enumerate(preds, 1)
            ],
        }
    elif args.cmd == "plan":
        _, planner = _load(args.algorithm)
        result = planner.plan(
            args.smiles, max_depth=args.max_depth,
            exclude_target=args.exclude_target,
        )
        out = {
            "target": args.smiles,
            "algorithm": args.algorithm,
            "solved": result.solved,
            "routes": [r.to_dict() for r in result.routes[: args.max_routes]],
        }
    elif args.cmd == "score":
        from synomega.synthesizability import SynthesizabilityScorer

        _, planner = _load(args.algorithm)
        report = SynthesizabilityScorer(planner).score(
            args.smiles, max_steps=args.max_steps,
            exclude_target=args.exclude_target,
        )
        out = report.as_dict()
    else:  # pragma: no cover
        p.error("unknown command")

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
