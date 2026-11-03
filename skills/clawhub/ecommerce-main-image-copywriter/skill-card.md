## Description:

基于用户提供的商品资料或抖音、小红书商品详情，提炼主图标题、副标题、卖点短句和配图建议，并可按需参考少量同类商品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商卖家和商品营销人员，依据用户提供的商品事实或支持平台的商品详情，撰写可用于商品主图的标题、副标题、卖点短句及配图建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups send product links, IDs, or search terms to SocialDataX and may consume API credits.

Mitigation: Avoid confidential inputs; use supplied product information when it is sufficient, and make online lookups only when needed for supported product details or requested comparisons.

Risk: The API key must be available to online CLI calls, and the external CLI code is not bundled or verified.

Mitigation: Protect the stored API key and consider using a reviewed, pinned CLI version in a restricted environment.

Risk: Draft marketing copy may include claims or changeable product details that need confirmation.

Mitigation: Check each claim against user-provided information or retrieved product details, keep unsupported facts out of the copy, and verify prices, offers, specifications, and other changeable details before publication.

## Reference(s):

- [SocialDataX API Key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/ecommerce-main-image-copywriter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with product image titles, subtitles, short selling points, and visual suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to three copy concepts; each has up to three short selling points and may note factual support or missing information.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
