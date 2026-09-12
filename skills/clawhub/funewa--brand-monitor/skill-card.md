## Description:

亚马逊品牌口碑监控 helps operators continuously collect and analyze Amazon ASIN reviews, track rating and negative-topic changes, surface review alerts, and compare competitor feedback; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and brand operators use this skill to monitor product review sentiment, identify repeated low-star complaints, compare competitors, and turn review evidence into reports and operating guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can consume ARI credits for review collection or analysis, including when server-side auto-confirm rules apply.

Mitigation: Use "只报价，不执行" for quote-only sessions or "以后每次扣点前先问我" to require confirmation before credit-consuming actions.

Risk: The skill stores and uses a local ARI API key and can be pointed at a custom ARI endpoint.

Mitigation: Do not paste API keys into chat or reports, and avoid custom ARI_BASE_URL settings unless the endpoint is controlled and intentionally authorized.

Risk: Recurring monitoring can create ongoing review-collection costs.

Mitigation: Review schedule costs before enabling watches or recurring collection, and keep schedules manual when continuous monitoring is not required.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, concise text summaries, JSON-backed CLI results, and local CSV, Markdown, or HTML exports when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid review collection and analysis may consume credits under account confirmation rules.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
