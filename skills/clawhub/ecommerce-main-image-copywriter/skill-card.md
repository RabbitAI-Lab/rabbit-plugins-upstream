## Description:

当用户需要提炼商品主图卖点、主副标题或安排商品图片信息层次时，基于商品资料或受支持的平台商品信息提供文案与配图建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者和商品内容创作者，基于用户提供的资料或请求查询的抖音、小红书商品信息，编写主图标题、副标题、卖点短句与配图建议，并列明依据和待补信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups send product URLs or IDs and search terms to SocialDataX and may consume paid credits; the API key is sensitive.

Mitigation: Prefer user-provided product information when sufficient; before online lookup, make the data sharing and possible credit use clear, keep SOCIALDATAX_API_KEY private, and consider a reviewed, pinned CLI version.

## Reference(s):

- [SocialDataX service and API key access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown table with copy-ready product copy and supporting notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to three copy concepts; each includes factual support and missing-information notes, subject to user instructions.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
