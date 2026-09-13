## Description:

Helps Amazon sellers use ARI-collected review data to diagnose product issues, monitor review trends, compare competitors, and generate VOC or operations reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to turn collected Amazon review data into concise diagnostics, VOC reports, competitor comparisons, trend checks, listing guidance, and monitoring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI workflows can spend credits through explicit confirmation or account auto-confirm rules.

Mitigation: Set the account to ask before paid actions when needed, use quote-only flows for estimates, and review credit use before approving reports.

Risk: Inherited ARI_BASE_URL or ARI_WEB_URL settings could direct API or web traffic away from the official ARI service.

Mitigation: Use the default ARI endpoint unless the user intentionally runs a trusted self-hosted endpoint and has explicitly enabled ARI_ALLOW_CUSTOM_BASE=1.

Risk: Monitoring, schedule, or competitor-tracking changes can affect future collection costs.

Mitigation: Review schedule and watch changes, including returned cost notes, before enabling recurring collection.

Risk: Reports are based on ARI-collected Amazon review samples and may not cover all reviews, all variants, or enough history for reliable trends.

Mitigation: Check sample size, site, date window, and stated coverage limits before using conclusions for business decisions.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Amazon Review Assistant User Guide](artifact/使用说明.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/seller-assistant)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, concise text answers, JSON command output, and local export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, sample ranges, credit usage, account status, and saved export paths.]

## Skill Version(s):

1.4.8 (source: server release, frontmatter, _meta.json, scripts/ari.py VERSION, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
