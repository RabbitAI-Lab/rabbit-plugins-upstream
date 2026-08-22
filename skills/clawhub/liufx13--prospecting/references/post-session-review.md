# Post-Session Review & Learning Integration

> **Note**: This is a meta-process document, NOT part of the prospecting skill execution flow. It describes what the AI assistant should do after completing a prospecting batch to abstract learnings and improve future sessions.

## When to Run

After every batch search completes and outputs are delivered to the user.

## Actions

### 1. Coverage Gap Report

Generate a `coverage-report.json` in the batch directory documenting:
- Which center+keyword combinations returned zero results
- Which auto-adjustments were applied (keyword swaps, satellite centers, brand additions)
- Estimated coverage percentage of target businesses in the area
- Known gaps that could not be filled (e.g., Google Maps restricted view, small markets)

This report helps users assess completeness without manual inspection.

See [references/coverage-report.md](references/coverage-report.md) for the full schema.

### 2. Chain Brand Learning

Update `chain-brands-detected.json` (per session, then merged to global):
```json
{
  "session": "houston-tx-2026-05-23",
  "newly_detected": [
    {"brand": "Caliber Collision", "locations": 10, "tier": "连锁-高端"},
    {"brand": "CARSTAR", "locations": 7, "tier": "连锁-中高端"},
    {"brand": "Crash Champions", "locations": 5, "tier": "连锁-中端"}
  ],
  "updated_global": true
}
```

If a brand appears in >2 locations, add it to the known chain list for future searches.

### 3. Memory Update

Append a concise learning summary to `memory/YYYY-MM-DD.md` under `Prospecting Skill Learnings`:
- New keywords that proved effective
- New center points discovered for a city
- Filter false-positives and how they were corrected
- Chain brands detected
- Any skill bugs or edge cases encountered

Also update `MEMORY.md` with key milestones.

This ensures cross-session learning and continuous improvement.

## Example: Houston 2026-05-23

**Key learnings captured**:
1. Filter false-positives are common (>20% threshold needs auto-relax)
2. Suburban expansion essential for large metros (6→11 centers, 50→90 prospects)
3. Keyword swapping fixes zero-result centers ("auto body shop" → "collision center")
4. Brand direct search catches missing chains (CARSTAR 7, Gerber 2)
5. Coverage gap reporting helps users assess completeness
6. Chain brand learning should be persistent across sessions

**Skill improvements applied**:
- Added Step 0: Self-Diagnostic & Adaptive Search Design
- Updated search-strategy.md with auto-expansion triggers
- Added references/coverage-report.md with schema
- Added 5 new Critical Rules (#14-#18)
- Bumped version to v2.0.0

---

*This document is for AI assistant self-improvement, not user-facing skill execution.*