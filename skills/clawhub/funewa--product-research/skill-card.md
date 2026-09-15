## Description:

Product Research helps agents validate Amazon product opportunities with ARI review data by surfacing customer complaints, unmet needs, buying motives, trends, competitor comparisons, and exportable reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to research product niches, validate demand, compare competitors, monitor review changes, and turn customer review evidence into product, listing, and operations decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI review collection or analysis can consume account credits, including cases where account-level auto-confirm rules allow execution.

Mitigation: Ask for quotes before execution when checking cost, set the account to require approval for every paid operation if desired, and confirm credit use before continuing.

Risk: Persistent account settings can change how future paid actions are confirmed.

Mitigation: Review and explicitly set the desired confirmation behavior before using paid workflows.

Risk: Exports can write report or review data to local files.

Mitigation: Keep ARI_EXPORT_DIR away from sensitive locations and review export paths before writing files.

Risk: Local API key storage can expose credentials if the config file is not private.

Mitigation: Ensure ~/.ari/config.json is a normal private file before saving an ARI API key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-research)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI User Guide](artifact/使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, CSV or HTML exports]

**Output Format:** [Markdown and concise text summaries, with CLI commands, JSON-backed results, and optional CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite sample scope and review evidence; paid actions may require confirmation or may execute under account-level auto-confirm rules.]

## Skill Version(s):

1.4.11 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
