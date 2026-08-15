## Description:

面向汽服、轮胎和润滑油品牌，使用高德地图复制的地点名称和地址文本与店店通已发布门店快照生成门店网络、区域覆盖和位置画像分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze automotive aftermarket brand store networks, regional coverage, nearby stores, and site-screening context from published DDT API snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may send coordinates or address-derived location context to the DDT API service.

Mitigation: Use only necessary location inputs, avoid sensitive personal or proprietary site data, and disclose when analysis depends on DDT API responses.

Risk: API credentials could be exposed if pasted into chats, files, logs, or generated responses.

Mitigation: Keep DDT_API_KEY in the local environment or a controlled secret store and never include real keys in skill text or user-facing output.

Risk: Incomplete coverage, truncated previews, or unsupported brands could lead to overstated business conclusions.

Mitigation: Check API ok status, coverage fields, data version, and preview.truncated before concluding; label missing coverage as unavailable and stop unsupported conclusions instead of filling gaps.

## Reference(s):

- [店店通开放平台](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-amap-auto-network)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with concise conclusions, key metrics, coverage notes, limited store details when requested, and optional curl examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DDT API responses as the source of business conclusions and avoids exposing API keys, storage IDs, supplier fields, internal fields, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
