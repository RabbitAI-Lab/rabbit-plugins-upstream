## Description:

汽服渠道的品牌规模、省市覆盖、服务类型与竞争格局分析。可将百度地图中复制出的地点名称和地址文本作为地点输入；基于店店通已发布门店快照生成可核验结论。本 Skill 非百度地图官方产品，和百度地图不存在合作、授权或数据来源关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, channel planners, and agents use this skill to analyze automotive aftermarket brand coverage, service categories, regional concentration, nearby stores, and competitive context from DDT-published snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill may send brand, address, coordinate, or store lookup queries to a third-party DDT/Open API service.

Mitigation: Confirm that this data sharing is acceptable before installation or use, and avoid submitting sensitive or unnecessary location details.

Risk: DDT API keys could be exposed if pasted into chat, logs, skill files, or source control.

Mitigation: Store API keys in controlled environment variables or a secret manager, and never include real keys in prompts, artifacts, logs, or commits.

Risk: Users may confuse the skill with an official Baidu Map product or assume its data comes from Baidu Maps.

Mitigation: Preserve the third-party disclosure and base conclusions only on DDT-published snapshots and returned API coverage fields.

## Reference(s):

- [DDT ClawHub API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-auto-channel)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with concise conclusions, metrics, coverage notes, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include limited public store details only when explicitly requested and supported by API responses.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
