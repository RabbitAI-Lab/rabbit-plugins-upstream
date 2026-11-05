## Description:

当用户需要做小红书博主画像、小红书博主信息、账号资料、创作者定位、粉丝规模判断或合作对象初筛时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, MCNs, content operators, and creators can look up a Xiaohongshu creator using a profile link, shared profile text, or account ID. They use the returned account details and engagement signals to understand creator positioning and screen potential collaboration partners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile lookups use a third-party service, may consume paid credits, and the external package implementation was not verified in this review.

Mitigation: Submit only the profile information needed for the lookup, keep the API key in the client's secret mechanism, and prefer a reviewed, fixed CLI version.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON profile data with a concise text or Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile fields and available engagement signals vary by account and API response.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
