## Description:

当用户需要提炼商品主图卖点、主副标题或安排商品图片信息层次时使用。提供商品链接或商品资料，输出主图标题、副标题、卖点短句与配图建议；可按需参考同类商品。在线商品能力支持抖音与小红书，已有资料可直接写作。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商经营者与营销人员，用于根据用户提供的商品资料或支持的平台商品信息，整理主图标题、副标题、卖点短句和画面建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly runs an unpinned `@latest` CLI, so the code may change between runs and execute with access to available credentials.

Mitigation: Review the CLI version and changes before use; where possible, use a reviewed version and limit credentials available to the execution environment.

Risk: The security review reports incomplete reference resolution, leaving some local references unchecked.

Mitigation: Review the CLI's behavior and any unresolved references before installing or using it, and share only product information appropriate for the online lookup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-main-image-copywriter)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with product copy and image suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usually provides three copy options; each includes a headline, subheadline, up to three supporting points, and a suggested visual.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
