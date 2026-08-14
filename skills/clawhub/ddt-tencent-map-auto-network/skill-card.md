## Description:

汽服、轮胎和润滑油品牌的门店网络、区域覆盖与位置画像分析；可将腾讯地图中复制出的地点名称和地址文本作为地点输入，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to evaluate automotive aftermarket brand store networks, regional coverage, service categories, surroundings, candidate sites, and selected store records from the DDT API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends brand names, coordinates, store IDs, or pasted address text to the DDT API service endpoint.

Mitigation: Confirm the DDT endpoint is trusted before installation and avoid sending confidential or unnecessary location and business details.

Risk: The skill requires DDT_API_KEY for API access.

Mitigation: Keep DDT_API_KEY only in the local or controlled runtime environment, and do not place the key in chats, logs, skill files, or version control.

Risk: Network, coverage, or preview limits can make analysis incomplete or misleading if treated as exhaustive.

Mitigation: Use only fields returned by the API, label uncovered data as unavailable, and narrow queries when preview.truncated is true.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-auto-network)
- [DDT API homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, and limited store details when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses published API snapshots only; avoids API keys, storage IDs, supplier fields, and unsupported metrics in responses.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
