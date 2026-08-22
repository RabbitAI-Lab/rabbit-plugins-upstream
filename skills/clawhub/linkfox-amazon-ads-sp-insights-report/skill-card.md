## Description:

亚马逊广告 Sponsored Products（SP）洞察报告技能，统一获取 Audience 受众细分表现和 Search Term Impression Share/Rank 搜索词展示份额/排名两类 Amazon Ads Reporting API v1 beta 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon Ads operators and agent users use this skill to fetch Sponsored Products audience performance and search term impression share or rank reports through LinkFox-backed Amazon Ads workflows. It helps route the right report type, poll asynchronous report generation, download CSV parts, and present concise report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Amazon Ads reporting requests and stores generated report files, so report data, cache files, API keys, and payment artifacts may be sensitive.

Mitigation: Install only when LinkFox is trusted for Amazon Ads reporting data, keep generated files and environment variables protected, and avoid exposing report outputs or credentials in shared logs.

Risk: The package includes account login, API-key generation, and payment workflows beyond simple report retrieval.

Mitigation: Prefer self-service account setup where possible, review onboarding steps before use, and confirm billing actions explicitly before running payment-related commands.

Risk: Custom LINKFOX_* endpoint overrides could redirect requests to an unintended service.

Mitigation: Use the default LinkFox endpoints unless the operator controls and trusts the override endpoint.

Risk: Amazon Reporting API v1 is documented as open beta, so account access, fields, limits, and async generation behavior may vary.

Mitigation: Treat HTTP 403, 429, failed reports, empty reports, and still-processing reports according to the skill guidance; do not fabricate replacement v3 data or broaden dates automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-sp-insights-report)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Amazon Ads SP insight report API reference](artifact/references/api.md)
- [Sponsored Products Audience Reporting API v1 reference](artifact/references/sp-audience-reporting-v1.md)
- [Sponsored Products Search Term Impression Share Reporting API v1 reference](artifact/references/sp-search-impression-share-v1.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON files and concise terminal summaries, with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete report responses and downloaded CSV parts under the current workspace; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
