---
name: feature-flags
description: Remote feature flag / toggle system for AI agents — enable/disable features without redeploy. Distilled from Claude Code GrowthBook integration.
metadata:
  openclaw:
    requires:
      bins: [python3]
---

# Feature Flags

Distilled from Claude Code GrowthBook integration. Remote feature toggle system
that lets you enable/disable features, run A/B tests, and push configuration
updates without redeploying.

## When to use

- Roll out new features gradually (10% → 50% → 100%)
- Kill switch for problematic features
- A/B test different behaviors
- Per-user/per-org feature gating
- Remote configuration without redeploy

## How it works

1. **Flag Definitions** — JSON/YAML file defining all feature flags
2. **Remote Polling** — Optional HTTP endpoint for remote flag updates
3. **Local Override** — CLI to override flags for testing
4. **Evaluation** — Check flag state with user/org context

## Usage

`ash
# Check a flag
python3 {baseDir}/flags.py --check new-ui

# List all flags
python3 {baseDir}/flags.py --list

# Override a flag locally
python3 {baseDir}/flags.py --override new-ui=true

# Set up remote polling
python3 {baseDir}/flags.py --poll-url http://localhost:8080/flags

# Export flags as JSON
python3 {baseDir}/flags.py --export
`

## Flag definition format

`json
{
  "new-ui": {
    "default": false,
    "description": "New UI redesign",
    "rules": [
      {"condition": "user_id == 'admin'", "value": true},
      {"condition": "org == 'beta'", "value": true}
    ]
  },
  "experimental-search": {
    "default": false,
    "rollout": 0.1,
    "description": "Experimental search v2 (10% rollout)"
  }
}
`

## Algorithm reference

Based on Claude Code GrowthBook integration:
- JSON-based flag definitions
- Remote polling with configurable interval
- User/org context evaluation
- Gradual rollout (percentage-based)
- Forced override for testing
- Feature usage tracking