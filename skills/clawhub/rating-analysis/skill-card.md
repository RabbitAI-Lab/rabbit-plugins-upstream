## Description:

Analyzes an Amazon ASIN's star-rating distribution, rating trend, low-star timing, and likely causes of rating decline using ARI-collected review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to diagnose product rating structure, review trends, low-star review clusters, competitor comparison signals, and listing or product-improvement opportunities from ARI-collected Amazon review samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broader ARI account, billing, monitoring, export, and workflow actions than a simple star-rating summary suggests.

Mitigation: Review the listed capabilities, billing rules, and auto-confirm setting before installation or first use.

Risk: Paid collection or AI analysis can consume ARI credits, and some flows may auto-confirm under account rules.

Mitigation: Use quote-only paths when pricing is requested, require explicit confirmation when needed, and configure auto-confirm to always ask if that matches the user's preference.

Risk: API keys could be exposed if pasted into chat, saved in a packaged directory, or sent to an unintended endpoint.

Mitigation: Use browser setup or local user configuration, keep keys out of reports and command examples, and avoid custom ARI_BASE_URL values unless the endpoint is controlled and explicitly allowed.

Risk: Interrupted paid analyses or collection waits may already have charged credits and created reports.

Mitigation: Check existing reports or task status before retrying any confirmed paid operation.

Risk: Rating conclusions may be misleading when review samples, time windows, marketplace coverage, or variant coverage are limited.

Mitigation: State sample scope and time window, flag small samples, and avoid inferring missing variant or trend data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/rating-analysis)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing and plans](https://ari.funewa.com/zh/billing)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, concise text summaries, JSON command responses, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection or AI analysis may consume ARI credits, and conclusions depend on the available ARI-collected Amazon review sample.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, evidence.release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
