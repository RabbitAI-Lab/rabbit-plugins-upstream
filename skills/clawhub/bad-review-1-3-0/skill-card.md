## Description:

Analyzes Amazon 1-3 star reviews for a specified ASIN to identify recurring causes such as quality issues, shipping damage, description mismatch, and usage confusion, then summarizes improvement opportunities for product teams and sellers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to collect and analyze Amazon review data, generate VOC and comparison reports, monitor negative-review alerts, and prioritize listing or product improvements. It requires an ARI API key and may consume ARI credits for collection, analysis, leaderboard, and advice commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key and can send Amazon review data to the configured ARI service endpoint.

Mitigation: Install and run it only if you trust ARI/funewa, and avoid setting ARI_BASE_URL or ARI_WEB_URL unless the endpoint is intentionally trusted.

Risk: Some collection, analysis, leaderboard, and advice commands can consume ARI credits when run with --confirm.

Mitigation: Review quoted costs before adding --confirm, and verify report history before retrying interrupted paid operations.

Risk: Workbench status updates and alert read commands can change state in the user's ARI account.

Mitigation: Confirm the intended account and action before marking alerts as read or changing review workflow status.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Server-resolved GitHub provenance](https://github.com/funewa/amazon-bad-review/tree/main/bad-review-1.3.0)
- [ClawHub skill release page](https://clawhub.ai/funewa/skills/bad-review-1-3-0)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON command results, CSV or Markdown/HTML exports, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include ASIN, site, sample size, reporting window, reportId, creditsUsed, current balance, and reportUrl when returned by ARI.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
