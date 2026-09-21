## Description:

ARI helps Amazon sellers collect and analyze reviews for ASINs, generate VOC and deeper insight reports, compare competitors, monitor product changes, handle negative-review alerts, and export review or report files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn ARI-collected review data into consumer insights, pain points, trend summaries, competitor comparisons, listing suggestions, alerts, and exportable reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger billable ARI collection or analysis workflows, and server-side auto-confirm behavior may allow some paid operations to run without a local confirmation step.

Mitigation: Review quoted costs, balances, and confirmationRequired or autoConfirmed results before paid work; set auto-confirm off when every charge should require explicit approval.

Risk: Schedule, competitors, and watch commands can create or remove ongoing account-side monitoring relationships.

Mitigation: Confirm the ASIN, site, cadence, cost, competitor relationship, and watch id before allowing an agent to run monitoring management commands.

Risk: The skill uses an ARI API key and account data.

Mitigation: Install only when the publisher is trusted with ARI account access, keep API keys out of chat and reports, and use the browser authorization flow or local hidden input for setup.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Usage Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/sellerari)
- [Publisher Profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON summaries, shell command guidance, configuration instructions, CSV exports, and Markdown or HTML report exports depending on the workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses the official https://ari.funewa.com service for account, review-analysis, reporting, export, alert, and monitoring workflows.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
