from __future__ import annotations

import json
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parent.parent / "references" / "market_entry.json"


def main() -> None:
    try:
        from second_perspective import IntelligentDecisionHub
        from second_perspective.models import HubAnalysisRequest
    except ImportError:
        sys.exit(
            "Engine not installed. Install nomos-decision-engine from the "
            "upstream repository (see references/README.md) before running."
        )

    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    request = HubAnalysisRequest.model_validate(
        {
            "decision": data,
            "scenarios": [
                {
                    "id": "SC1",
                    "name": "Critical partner assumption fails",
                    "failed_assumption_ids": ["A1"],
                },
                {
                    "id": "SC2",
                    "name": "Partner capital requirement exceeds budget",
                    "metric_overrides": {"S2": {"capital_required": 6000000}},
                },
            ],
        }
    )
    report = IntelligentDecisionHub().analyze(request)
    print(report.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
