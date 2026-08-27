## Description:

用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询，覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up read-only Weibo creator profile information from SocialDataX by creator user ID or profile URL. It helps report available profile facts such as platform IDs, bio, verification, follower counts, IP location, and gender while keeping factual data separate from interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCIALDATAX_API_KEY and network requests to retrieve Weibo profile data.

Mitigation: Install and run it only when the user trusts SocialDataX, and keep the API key in the runtime environment rather than embedding it in skill files.

Risk: The direct CLI path runs an npm package through npx.

Mitigation: Review npm package provenance and local execution permissions before use, as recommended by the security guidance.

Risk: Using the skill for account-changing workflows would exceed its stated read-only boundary.

Mitigation: Use it only for profile lookup and do not use it for login, posting, liking, commenting, or other account changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON profile data from the SocialDataX CLI or MCP tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and SOCIALDATAX_API_KEY; the skill is intended for read-only profile lookup.]

## Skill Version(s):

0.1.18 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
