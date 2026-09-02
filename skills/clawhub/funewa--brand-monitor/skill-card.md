## Description:

This skill helps Amazon sellers monitor multiple ASINs, track review sentiment and ratings, detect negative-review spikes, compare competitors, and generate review insight reports through ARI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, brand operators, and ecommerce teams use this skill to monitor product-review reputation, receive negative-review alerts, compare competitors, and turn collected Amazon review data into VOC reports, listing recommendations, exports, and response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key and Amazon review workflow data with a third-party service.

Mitigation: Install only when ARI/funewa is trusted, keep the key in environment or user-local configuration, and avoid storing it on shared machines, synced folders, reports, screenshots, or public documents.

Risk: Paid commands and recurring schedules can consume credits, including future collection charges for scheduled ASIN or competitor tracking.

Mitigation: Review quoted costs and account balance before confirming paid commands, require explicit confirmation before appending --confirm, and explain schedule or competitor-tracking costs before enabling them.

Risk: A network interruption after a paid command may occur after the service has already charged credits or archived a report.

Mitigation: Check existing reports or operation status before retrying interrupted paid commands, and retry only when no completed result exists.

Risk: Changing the ARI base URL can redirect authenticated requests away from the official service.

Mitigation: Use the official ARI endpoint by default and allow a custom base URL only when ARI_ALLOW_CUSTOM_BASE=1 is intentionally set for a trusted development or self-hosted environment.

Risk: Review analysis can be misleading when samples are small, collection windows are limited, or competitor data is incomplete.

Mitigation: State sample size and window, distinguish raw API data from inference and strategy, avoid fabricating missing fields, and mark comparisons as not comparable when one side lacks sufficient data.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Skill README](artifact/README.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/brand-monitor)
- [ARI API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports, JSON command results, CSV/Markdown/HTML exports, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid or mutating actions require explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release evidence, SKILL.md frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
