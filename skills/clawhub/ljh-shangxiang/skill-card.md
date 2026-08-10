## Description:

商详页说服地图把定位、卖点、场景、人群和验证证据编排成商品详情页策略、逐屏结构与内容文档，并可按需输出低保真 HTML。

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce, brand, and content teams use this skill to turn existing product positioning, selling points, scenarios, audience insights, and validation evidence into a product-detail page persuasion map. The output supports page strategy, screen-by-screen content planning, evidence placement, production handoff, and optional low-fidelity HTML structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a first-run marker in the user's home directory and may read or update a local ljh-档案 brand archive for continuity.

Mitigation: Use the skill only in a project directory where local archive behavior is acceptable, and explicitly instruct the agent not to use archives when local persistence is not desired.

Risk: Product claims, prices, credentials, platform rules, or evidence could be misleading if the user has not provided a source.

Mitigation: Keep unsupported facts as pending items, require sources for claims and commercial terms, and review the strategy before using it in production content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-shangxiang)
- [Publisher profile](https://clawhub.ai/user/handsomeng)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown strategy document with tables and optional low-fidelity HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or update a local brand archive when the user permits archive use; uses explicit pending-verification markers for unsupported facts, prices, claims, platform rules, and evidence.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
