## Description:

Seller Assistant helps Amazon sellers use ARI review data to analyze owned and competitor products, generate VOC and insight reports, monitor review changes, and export review or report files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to diagnose review trends, low-star feedback, competitor differences, keyword opportunities, and product or listing improvements from ARI-collected review data. It can also guide paid report generation, monitoring, alert review, and exports when the user's ARI account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI review-analysis workflows can spend account credits without fresh confirmation when account rules allow automatic confirmation.

Mitigation: Set autoconfirm to always ask or use quote-only requests before paid workflows, then review the quoted cost and balance before confirming.

Risk: Exports can overwrite local files or use an overly broad export directory.

Mitigation: Use a dedicated export directory, keep ARI_EXPORT_DIR narrow, and avoid exporting over existing or important project files.

Risk: The skill requires connecting an ARI account and using an ARI API key.

Mitigation: Use the browser authorization flow when possible, do not paste API keys into chat, and revoke or rotate keys from the ARI account page when access should end.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/seller-assistant)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI User Guide](artifact/使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline shell commands and links; ARI exports may produce CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid ARI workflows may spend account credits according to the user's account confirmation rules.]

## Skill Version(s):

1.4.11 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
