## Description:

Amazon Voc helps agents use ARI to collect Amazon reviews and produce VOC reports covering pain points, purchase drivers, buyer personas, trends, competitor comparisons, alerts, and listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and their agents use this skill to authorize ARI, collect or inspect Amazon review data, and generate VOC analysis for product operations, listing optimization, monitoring, and competitor comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI analysis or collection can spend credits without a fresh confirmation when account auto-confirm rules apply.

Mitigation: Before paid analysis, ask for quote-only behavior, disable or limit auto-confirm, or require explicit confirmation before every credit-deducting action.

Risk: The skill uses an ARI API key and stores local configuration that could be exposed if the host account or config file is shared.

Mitigation: Protect ~/.ari/config.json, avoid sharing API keys in chat or reports, and revoke the ARI API key from the ARI account page when it is no longer needed.

Risk: VOC conclusions may be incomplete or misleading when ARI has limited, stale, or non-representative review samples.

Mitigation: Report the sample scope, avoid unsupported trend claims, and collect or refresh review data before relying on recommendations for business decisions.

## Reference(s):

- [Server-resolved GitHub source: funewa/Amazon-variant-analysis](https://github.com/funewa/Amazon-variant-analysis)
- [ClawHub listing: Amazon Voc](https://clawhub.ai/funewa/skills/amazon-variant-analysis)
- [ARI CLI and API Reference](references/reference.md)
- [Usage Guide](使用说明.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Natural-language analysis and Markdown reports, with shell commands and JSON, CSV, Markdown, or HTML outputs when relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some ARI analysis or collection actions can spend account credits.]

## Skill Version(s):

0.1.4 (source: server release metadata); artifact package reports 1.4.10

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
