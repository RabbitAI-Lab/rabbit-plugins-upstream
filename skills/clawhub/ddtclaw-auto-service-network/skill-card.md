## Description:

用已发布的汽车后市场门店快照，快速分析品牌网络、服务类型、区域覆盖、周边画像、竞对与候选点，帮助市场、渠道、销售和拓展团队获取可执行的攻店与选址线索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External business, market, channel, sales, and expansion teams use this skill to query published auto-service store-network data for brand coverage, regional distribution, service mix, nearby stores, competitor context, and candidate-site screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if DDT_API_KEY is pasted into chat, logs, or version control.

Mitigation: Keep DDT_API_KEY in the local or controlled runtime environment and do not include real keys in prompts, responses, logs, or repositories.

Risk: Business conclusions may be overstated when API coverage is incomplete, a preview is truncated, or a brand or store is not found.

Mitigation: Use only returned API fields, check ok, coverage, and preview.truncated indicators, and label unavailable coverage as not covered instead of inferring missing values.

Risk: The skill depends on a third-party API provider for published auto-service store network data.

Mitigation: Confirm the API provider is trusted before installation and stop business conclusions when authentication, quota, or upstream service errors prevent reliable retrieval.

## Reference(s):

- [DDTClaw Auto-Service API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddtclaw-auto-service-network)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise business conclusions, key metrics, coverage notes, and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be limited to published aggregate data and user-requested small store previews; API keys, supplier fields, storage IDs, and unsupported conclusions are excluded.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
