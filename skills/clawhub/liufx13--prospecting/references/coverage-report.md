# Coverage Report Format

## Purpose

The `coverage-report.json` is generated automatically after all search passes complete. It documents:
1. Which center+keyword combinations returned zero results
2. Which auto-adjustments were applied
3. Estimated coverage percentage of target businesses in the area

This helps users assess completeness without manual inspection and feeds into the self-optimization loop for future runs.

## Schema

```json
{
  "batch_id": "houston-tx-2026-05-23",
  "generated": "2026-05-23",
  "city_population": "7M",
  "target_prospects": 80,
  "actual_prospects": 90,
  "coverage_estimate": "65-75%",
  "passes": [
    {
      "pass": 1,
      "centers_searched": 6,
      "keywords_used": 6,
      "unique_prospects_found": 50,
      "zero_result_combos": [
        {"center": "The Woodlands", "keyword": "auto body shop", "action": "swapped to collision center"},
        {"center": "Cypress", "keyword": "collision repair", "action": "swapped to body shop"}
      ],
      "low_yield_keywords": [
        {"keyword": "paint shop", "results": 8, "action": "too broad, mixed with house painting"}
      ]
    },
    {
      "pass": 2,
      "centers_searched": 6,
      "keywords_used": 5,
      "unique_prospects_added": 18,
      "auto_adjustments": [
        {"type": "keyword_swap", "from": "auto body shop", "to": "collision center", "center": "The Woodlands"},
        {"type": "keyword_swap", "from": "collision repair", "to": "body shop", "center": "Cypress"},
        {"type": "brand_add", "brand": "Caliber", "center": "Houston"},
        {"type": "brand_add", "brand": "CARSTAR", "center": "Houston"}
      ]
    },
    {
      "pass": 3,
      "centers_searched": 11,
      "keywords_used": 3,
      "unique_prospects_added": 22,
      "auto_adjustments": [
        {"type": "suburban_expansion", "new_centers": ["Pearland", "Pasadena", "Galveston", "Spring", "Humble"], "reason": "initial 6 centers yielded only 50 prospects, below 80 target for 7M metro"}
      ]
    }
  ],
  "remaining_gaps": [
    {"center": "Galveston", "issue": "small market, only 6 listings", "severity": "low"},
    {"center": "Spring", "issue": "Caliber-dominated, 8 listings", "severity": "low"}
  ],
  "filter_false_positives": [
    {"name": "Maaco", "reason": "incorrectly filtered in v1", "corrected_in": "v2"},
    {"name": "Gerber", "reason": "incorrectly filtered in v1", "corrected_in": "v2"},
    {"name": "Crash Champions Spring", "reason": "incorrectly filtered in v1", "corrected_in": "v2"}
  ],
  "chain_brands_detected": [
    {"brand": "Caliber Collision", "locations": 10, "tier": "连锁-高端"},
    {"brand": "CARSTAR", "locations": 7, "tier": "连锁-中高端"},
    {"brand": "Crash Champions", "locations": 5, "tier": "连锁-中端"},
    {"brand": "Maaco", "locations": 6, "tier": "连锁-中端"},
    {"brand": "Gerber", "locations": 2, "tier": "连锁-中高端"}
  ],
  "notes": "Houston metro fully covered with 11 centers. 90 prospects exceeds 80 target. Coverage estimate 65-75% based on known market size."
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `batch_id` | string | Unique identifier for the search batch |
| `generated` | string | Date of generation |
| `city_population` | string | Population of target city/metro |
| `target_prospects` | number | Target number of prospects based on city size |
| `actual_prospects` | number | Actual unique prospects found |
| `coverage_estimate` | string | Estimated percentage of total market covered |
| `passes` | array | Details for each search pass |
| `remaining_gaps` | array | Gaps that could not be filled |
| `filter_false_positives` | array | Valid prospects that were incorrectly filtered |
| `chain_brands_detected` | array | Chain brands discovered during search |
| `notes` | string | Human-readable summary |

## Usage

1. **Review after run**: Check `coverage_estimate` to see if search was comprehensive enough
2. **Feed into next run**: Use `remaining_gaps` and `chain_brands_detected` to improve Step 0
3. **Share learnings**: Copy `chain_brands_detected` to global `chain-brands-detected.json`
4. **Update MEMORY.md**: Summarize key learnings for cross-session improvement

## Version

- **Version**: 1.0.0
- **Date**: 2026-05-23
- **Scope**: All B2B proactive prospecting projects