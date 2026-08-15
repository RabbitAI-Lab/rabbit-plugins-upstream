## Description:

当用户需要做小红书博主画像、小红书博主信息、账号资料、创作者定位、粉丝规模判断或合作对象初筛时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External teams such as brands, MCNs, content operators, and creators use this skill to look up Xiaohongshu creator profile data and support creator positioning, audience-scale judgment, and collaboration shortlisting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm package and uses SOCIALDATAX_API_KEY for SocialDataX requests.

Mitigation: Install only after confirming trust in SocialDataX, configure only the required API key, and avoid providing unrelated private data.

Risk: Creator profile results may be used for business screening decisions and can mix observed profile facts with strategic interpretation.

Mitigation: Keep visible facts separate from judgments and review profile outputs before using them in collaboration or outreach decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-creator-profile-insights)
- [SocialDataX AI homepage](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and SOCIALDATAX_API_KEY; the integration is described as read-only creator profile lookup.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
