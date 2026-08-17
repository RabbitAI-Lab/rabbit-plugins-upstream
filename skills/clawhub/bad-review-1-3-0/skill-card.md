## Description:

Analyzes 1-3 star Amazon reviews for a specified ASIN, ranks recurring causes such as quality issues, shipping damage, description mismatch, and usage confusion, and provides product and listing improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product managers, and marketplace operators use this skill to collect and analyze low-star review data for ASINs, identify return and negative-feedback drivers, compare competitors, and plan product or listing improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated ARI API traffic can be redirected if ARI_BASE_URL is set.

Mitigation: Leave ARI_BASE_URL unset for normal use, and set it only when intentionally pointing the skill at a trusted ARI development server.

Risk: Use can expose ASINs, review data, generated reports, account metadata, and the ARI API key to ARI/funewa.

Mitigation: Install and use the skill only when the user accepts that trust relationship, and keep the API key out of public reports, command examples, screenshots, and source control.

Risk: Commands using --confirm can spend credits, while --mark-read and --set-status can change remote workflow state.

Mitigation: Quote paid operations first, require explicit user confirmation before adding --confirm, and review target ASINs, report IDs, review IDs, and state changes before execution.

Risk: Exports can write review CSVs or report files to local storage.

Mitigation: Choose output paths deliberately, avoid writing sensitive exports into shared workspaces, and verify generated files before sharing.

## Reference(s):

- [Server-resolved source: funewa/amazon-bad-review](https://github.com/funewa/amazon-bad-review/tree/main/bad-review-1.3.0)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/bad-review-1-3-0)
- [ARI CLI and API reference](references/reference.md)
- [ARI service](https://ari.funewa.com)
- [ARI API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown analysis reports, structured JSON from CLI commands, CSV exports, and HTML or Markdown report exports when supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; fee-based operations require explicit user confirmation before spending credits.]

## Skill Version(s):

1.3.0 (source: artifact/SKILL.md frontmatter and artifact/_meta.json; ClawHub release version 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
