## Description:

使用高德地图地址文本和店店通已发布门店快照，分析餐饮连锁拓店机会区域、候选地址竞争和现场验证优先级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

餐饮连锁拓展、选址和销售团队可用此 skill 基于地址、品牌和区域条件生成拓店机会、竞品密度、候选点风险与现场验证优先级分析。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Restaurant brand names, candidate addresses, and related query details may be sent to gotoshop-ai.com when the skill uses the DDT API.

Mitigation: Avoid entering confidential expansion plans or sensitive candidate locations unless sharing them with that service is acceptable.

Risk: API keys could be exposed if copied into chat or output.

Mitigation: Store the DDT API key in the local DDT_API_KEY environment variable and do not display it in responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-amap-restaurant-expansion)
- [店店通 DDT Claw homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown business analysis with concise metrics, scope notes, and occasional bash or curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded DDT API queries, reports coverage and limits, and avoids exposing API keys or internal identifiers.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
