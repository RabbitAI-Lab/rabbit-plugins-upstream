## Description:

This skill helps Amazon sellers and ecommerce operators validate product opportunities by using ARI-collected Amazon review data to identify buyer complaints, purchase motivations, trends, competitor differences, and listing or product improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and product researchers use this skill to turn Amazon reviews into evidence-backed product research, VOC reports, competitor comparisons, keyword ideas, monitoring, alerts, and exportable reports. It is intended for commercial product selection and operations workflows where users need sample scope, costs, and limitations stated clearly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits automatically under server-side auto-confirm rules or after user confirmation.

Mitigation: Use strict spending language such as '以后每次扣点前先问我' or '只报价，不执行', review quoted credits and balance before paid actions, and avoid changing auto-confirm settings unless that is the user's explicit goal.

Risk: The skill uses an ARI API key and can read, report on, and export ARI/Amazon review data.

Mitigation: Authorize only through the ARI flow, do not paste API keys into chat or reports, revoke keys from the ARI account page when needed, and review exports before sharing them.

Risk: Custom ARI endpoint environment variables can redirect API-key-bearing requests if set incorrectly.

Mitigation: Use the official ARI endpoint for normal use, and set ARI_BASE_URL with ARI_ALLOW_CUSTOM_BASE only for an endpoint the user controls and understands.

Risk: Review analysis can be misleading when samples, time windows, variants, or competitor data are incomplete.

Mitigation: State sample size, site, time window, and known gaps in outputs; avoid firm trend or comparison claims when the available data is insufficient.

Risk: Monitoring and schedule changes can affect future data collection and recurring collection costs.

Mitigation: Require explicit user approval before schedule or watch changes, state the returned cost note, and keep manual, pause, resume, and delete controls visible to the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-research)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON summaries with occasional shell commands, local CSV/Markdown/HTML exports, and ARI report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state review sample scope, site, time window, report ID, credits used, and data limitations when available.]

## Skill Version(s):

1.4.8 (source: server release evidence, artifact frontmatter, _meta.json, CHANGELOG, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
