# Changelog

## 0.1.0

Initial standalone release of `text-to-infographic`.

Included:
- independent `SKILL.md` with infographic-first positioning
- `schemas/infographic-plan.schema.json`
- seven example infographic plans
- `scripts/validate_infographic_plan.py`
- `scripts/build_infographic_adapters.py`
- package-level README, skill card, and MIT-0 license

Design choices:
- one schema first, not multiple execution schemas
- no absolute coordinates in the plan layer
- adapter drafts for SVG / whiteboard / doc workflows
- strong separation from `text-to-comic`
