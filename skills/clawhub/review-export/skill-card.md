## Description:

Exports collected Amazon reviews for an ASIN to CSV and can generate ARI review analysis reports in Markdown or HTML for marketplace operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce teams use this skill to collect, analyze, monitor, and export Amazon review data for ASIN-level product decisions. It is intended for ARI-authorized accounts and may use account credits for collection or AI analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI credits may be spent without a fresh per-operation confirmation when ARI's remote auto-confirm policy allows it.

Mitigation: Review billing behavior before installation; tell the agent to set autoconfirm off before analyses, and say 'only quote, do not execute' when requesting pricing only.

Risk: Monitoring, competitor, and workbench commands can persistently change ARI account state.

Mitigation: Use those commands only after explicit user approval and verify the target ASIN, watch ID, competitor, or review ID before changing account state.

Risk: Analysis and exports depend on ARI-collected review samples and may not cover all Amazon reviews or all product variants.

Mitigation: Report sample size, review date range, collection scope, and variant limits; treat small samples or limited windows as directional evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-export)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant User Guide](使用说明.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing and plans](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Conversational guidance, Markdown reports, CSV exports, HTML or Markdown report files, and CLI JSON/status messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key or browser authorization; some collection, analysis, monitoring, leaderboard, and advice workflows can spend credits or change ARI account state.]

## Skill Version(s):

1.4.13 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
