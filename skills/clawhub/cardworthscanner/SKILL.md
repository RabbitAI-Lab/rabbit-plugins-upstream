---
name: cardworthscanner
description: "AI-assisted trading card game (TCG) price scanner, PSA/BGS/CGC grading ROI calculator, and card border centering inspector."
metadata:
  version: "1.0.1"
  homepage: "https://cardworthscanner.com"
  author: "CardWorthScanner Studio"
---

# CardWorthScanner TCG & Sports Card Grading Assistant

The **CardWorthScanner** skill equips AI agents with professional trading card valuation, optical centering calculation, and third-party authentication grading economics.

Live Web Workbench: [https://cardworthscanner.com](https://cardworthscanner.com)

---

## When to Use This Skill

1. **Card Grading Submission Decisions**: When a user asks "Should I grade this card with PSA, BGS, or CGC?", calculate expected return on investment (ROI) and minimum gem-mint probability required to break even.
2. **Centering Ratio Verification**: When a user provides optical border measurements (left/right and top/bottom borders) to predict PSA 10 (55/45 or better) vs BGS 9.5 (50/50) centering subgrades.
3. **TCG Market Value Comps**: When analyzing current market value spreads between raw cards and graded slabs across Pokemon TCG, MTG, Yu-Gi-Oh!, and Topps/Panini sports cards.

---

## Remote Endpoint Configuration

```json
{
  "mcpServers": {
    "cardworthscanner": {
      "url": "https://cardworthscanner.com/api/mcp"
    }
  }
}
```

---

## Official Reference

- **Interactive Card Centering & ROI Calculator**: [https://cardworthscanner.com](https://cardworthscanner.com)
- **PSA Grading Submission Standards**: [https://cardworthscanner.com/psa-grading-calculator](https://cardworthscanner.com/psa-grading-calculator)
- **TCG Market Scanner**: [https://cardworthscanner.com/card-scanner](https://cardworthscanner.com/card-scanner)
