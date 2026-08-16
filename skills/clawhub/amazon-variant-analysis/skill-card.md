## Description:

This skill uses ARI's Amazon review CLI to compare color, size, and specification variants under a parent ASIN, identify variants that hurt overall ratings, and surface high-performing variants for inventory and listing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and agents acting for those users use this skill to collect and analyze Amazon review data, compare variants or competitors, generate VOC and insight reports, and decide which variants to promote, fix, or de-emphasize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's real scope is broader than variant comparison and includes ARI account workflows, exports, alerts, and workbench status updates.

Mitigation: Install only when the broader ARI review-intelligence workflow is intended, and review commands such as --mark-read, --set-status, and export before execution.

Risk: ARI API keys can grant access to account data and paid analysis functions.

Mitigation: Keep the ARI API key private, use setup/configure or ARI_API_KEY without placing keys in reports or public files, and revoke keys from the ARI account page if exposed.

Risk: Paid collection, AI analysis, leaderboard, and advice commands can spend credits, and retrying interrupted paid flows can cause duplicate charges.

Mitigation: Run the quote or preview flow first, add --confirm only after explicit user approval, and check recent reports before retrying interrupted paid commands.

Risk: Changing ARI_BASE_URL can route credentials and requests to a nonstandard endpoint.

Mitigation: Avoid setting ARI_BASE_URL except in a trusted development environment.

## Reference(s):

- [ARI CLI and API reference](artifact/references/reference.md)
- [Server-resolved GitHub provenance](https://github.com/funewa/Amazon-variant-analysis)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/amazon-variant-analysis)
- [ARI API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON CLI responses, shell command examples, configuration steps, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some commands can spend ARI credits only after explicit --confirm, and export/configuration commands may write local files.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact version fields report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
