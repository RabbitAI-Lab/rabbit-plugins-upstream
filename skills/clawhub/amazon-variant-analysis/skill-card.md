## Description:

Compares Amazon parent-child ASIN variants by color, size, and specification to identify variants that depress ratings, variants that perform well, and actions for inventory or listing focus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to collect and analyze ARI review data for ASIN variants, compare color, size, and specification performance, and decide which variants to prioritize, fix, or de-emphasize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad ARI account, monitoring, export, and paid-operation capabilities beyond variant comparison.

Mitigation: Install only when that scope is acceptable, run account-impacting commands intentionally, and review command output before acting.

Risk: The skill uses an ARI API key and can read product, review, report, and account-related data.

Mitigation: Store the key only in ARI_API_KEY or the local user config, avoid sharing credentials in prompts or reports, and revoke or recreate keys if exposed.

Risk: Confirmed paid actions can spend ARI credits, and retrying interrupted paid commands may duplicate spending.

Mitigation: Require an explicit quote and confirmation step, then check existing reports or operation status before retrying interrupted confirmed commands.

Risk: Exports can write business review or report data to local files.

Mitigation: Limit exports to needed data and handle generated CSV, Markdown, or HTML files according to the user's data-handling requirements.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Web Application](https://ari.funewa.com)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/amazon-variant-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI/API responses may include JSON and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid actions require explicit confirmation before execution.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter and _meta.json report 1.4.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
