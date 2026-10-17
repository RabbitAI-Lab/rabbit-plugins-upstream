## Description:

Finds listed model API prices and free credits through Grandet and helps connect a selected provider to an AI app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanzohanzhe](https://clawhub.ai/user/hanzohanzhe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AI app users compare listed model API prices and free-credit offers, then optionally configure their app to use a chosen provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a provider can change an app's default model and cause future requests to spend credit at the selected provider.

Mitigation: Review the proposed config changes and backup before approving; confirm the provider and any paid test separately.

Risk: Installing the skill persists it across sessions and may send installation receipts to Grandet.

Mitigation: Install only if persistent use is wanted; use --no-telemetry to opt out of receipts.

Risk: Listed prices and provider quality may not reflect actual charges or service performance.

Mitigation: Check current units and provider terms before buying; do not treat a low listed price as proof of quality.

## Reference(s):

- [Grandet](https://grandet.ai)
- [Grandet API Price Finder on ClawHub](https://clawhub.ai/hanzohanzhe/skills/grandet-api-price-finder)
- [Price response guidance](artifact/references/response-format.md)
- [App connection guidance](artifact/references/host-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Concise text or Markdown with listed prices, links, and optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and availability depend on current Grandet listings; configuration changes require user approval.]

## Skill Version(s):

0.3.0-build.20261016.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
