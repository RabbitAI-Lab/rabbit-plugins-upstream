## Description:

餐饮连锁拓店选址专家，基于已发布门店快照分析区域扩张、候选点竞对密度与选址风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

拓展经理、选址团队和品牌负责人使用此 skill 查询已发布餐饮品牌快照，比较机会区域、候选地址周边竞争密度、选址风险和下一步实地验证重点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party restaurant data service and API key, which may involve usage costs, availability limits, or separate data terms.

Mitigation: Confirm trust in the gotoshop-ai.com service, review applicable data terms and costs, and keep DDT_API_KEY in local environment variables only.

Risk: The skill is not designed to work offline or provide complete raw store exports.

Mitigation: Use the aggregate endpoints and limited previews described by the skill, and ask users to narrow queries rather than assembling full store lists.

Risk: Restaurant expansion conclusions can be misleading if partial coverage, preview truncation, or missing capabilities are ignored.

Mitigation: Check response status, coverage period, capabilities, and truncation markers before giving business conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-restaurant-expansion-expert)
- [DDT homepage](https://gotoshop-ai.com/ddtclaw/)
- [DDT Open API key page](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown narrative with concise metrics, coverage notes, limited detail tables, and validation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scoped restaurant-data API responses; detailed store previews are limited and should not be expanded into bulk exports.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
