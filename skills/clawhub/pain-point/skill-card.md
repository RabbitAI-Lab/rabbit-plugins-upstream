## Description:

从 Amazon 评论中提炼买家痛点和未满足需求，按频次与情绪强度排序，并附原评论佐证。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to analyze review samples for recurring pain points, unmet needs, trends, competitor gaps, and listing or product improvement opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through collection and analysis flows, including documented auto-confirm paths that may run without a fresh prompt.

Mitigation: Review the account's auto-confirm setting before use, use quote-only requests when estimating cost, and set the account to ask before every paid action when predictable approval is required.

Risk: The skill can change ongoing account settings such as auto-confirm thresholds, scheduled collection, and watch configuration.

Mitigation: Require explicit user intent before changing settings, state the resulting rule or schedule back to the user, and periodically review active schedules and watch settings.

Risk: Custom ARI_BASE_URL or ARI_WEB_URL values can redirect authenticated requests away from the official ARI service.

Mitigation: Avoid custom ARI endpoints unless they are trusted HTTPS services controlled by the user, and only enable them with an intentional ARI_ALLOW_CUSTOM_BASE=1 setting.

Risk: Interrupted paid analysis or collection may already have generated a report or consumed credits.

Mitigation: Check existing reports or task status before retrying any paid operation, and only rerun after confirming that no result was created.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/pain-point)
- [使用说明](artifact/使用说明.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Conversational text, Markdown reports, JSON-derived summaries, shell command snippets, and optional exported CSV, Markdown, or HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis can consume ARI credits, and some exports depend on plan entitlements.]

## Skill Version(s):

1.4.8 (source: server release metadata, artifact frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
