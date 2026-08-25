## Description:

用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Kuaishou creator profiles, account basics, audience scale, and creator discovery candidates through SocialDataX using their own API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou creator keywords, profile URLs, or user IDs are sent to SocialDataX under the user's API key.

Mitigation: Install and run the skill only when that data sharing is acceptable for the user's account and workflow.

Risk: Returned profile data comes from a third-party API and may be incomplete or unsuitable as the sole basis for business decisions.

Mitigation: Verify important decisions independently and separate reported profile facts from strategic interpretation.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY and reports third-party Kuaishou creator profile data when available.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
