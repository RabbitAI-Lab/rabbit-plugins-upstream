## Description:

餐饮品牌竞对情报专家，分析品牌开关店、月末在营趋势、重点省市与竞争方向。适用于市场、战略和竞品团队监测对手扩张收缩、比较品牌网络并形成月度市场判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Market, strategy, and competitive-intelligence teams use this skill to monitor published restaurant-brand network changes, compare competitors over shared coverage windows, and turn store-opening, closure, regional, and trend signals into monthly market judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends restaurant competitor research requests to the gotoshop-ai.com DDT API and depends on a locally stored API key.

Mitigation: Confirm the external service is approved for the use case, store the API key only in a local environment variable, and do not reveal the key in outputs.

Risk: Competitor research prompts may include confidential expansion plans or sensitive addresses.

Mitigation: Avoid entering confidential plans or sensitive addresses unless the DDT service is approved for that data.

## Reference(s):

- [DDT Claw Homepage](https://gotoshop-ai.com/ddtclaw/)
- [DDT API Key Portal](https://gotoshop-ai.com/ddtclaw/open)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-restaurant-competitor-expert)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with concise metrics, coverage notes, and limited shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a DDT API key and external restaurant-network API; avoids exposing API keys, internal identifiers, and full store-list exports.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
