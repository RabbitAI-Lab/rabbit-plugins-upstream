## Description:

Review Alerts helps Amazon sellers use ARI to monitor subscribed ASINs for negative review spikes and rating drops, inspect supporting reviews, and generate review analysis, response guidance, and exportable reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and ecommerce teams use this skill to monitor review sentiment, investigate negative-review spikes, compare products, and produce operational guidance from ARI-collected review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an ARI account key to run paid analyses that consume credits.

Mitigation: Review quotes and confirmation prompts before approving paid actions, and use quote-only wording when only pricing is needed.

Risk: The skill sends Amazon ASIN and review data to ARI for analysis.

Mitigation: Install only when ARI account linking and ARI processing of the relevant review data are acceptable.

Risk: Account settings, monitoring, exports, and review status changes can persist beyond a single response.

Mitigation: Review requests to enable monitoring, change autoconfirm limits, export data, or update statuses before approving them.

Risk: Review analysis can be misleading when samples or time windows are limited.

Mitigation: Check the stated sample range, date window, and data limitations before using conclusions for product or marketplace decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-alerts)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI User Center](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or text responses with optional JSON CLI output and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and Amazon ASIN/site inputs; paid actions may consume ARI credits under account confirmation rules.]

## Skill Version(s):

1.4.11 (source: SKILL.md frontmatter, artifact/_meta.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
