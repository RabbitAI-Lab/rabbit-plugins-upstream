## Description:

用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up public Weibo creator profile details, account basics, audience scale, and related profile fields through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Weibo profile IDs or profile URLs to SocialDataX hosted services using the user's SocialDataX API key.

Mitigation: Confirm the user trusts SocialDataX and is comfortable sharing those identifiers before installing or running the skill.

Risk: The example command installs socialdatax-skills with @latest, which can reduce reproducibility.

Mitigation: Pin the npm package version when reproducible installs are required.

## Reference(s):

- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports profile facts separately from strategic interpretation when profile data is available.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
