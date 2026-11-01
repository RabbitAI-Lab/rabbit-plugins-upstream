## Description:

通过 SocialDataX 搜索 X/Twitter 帖子、查看详情和讨论，并查询创作者资料、帖子及其回复。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill for read-only X/Twitter research, including post search and details, discussion analysis, creator profiles, creator posts, and creator-authored replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, identifiers, and supplied URLs are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Avoid confidential queries and consider credit use before broad or paginated searches.

Risk: Exposure of SOCIALDATAX_API_KEY could enable unauthorized use of the account.

Mitigation: Keep the API key in a protected environment variable and out of prompts, logs, and generated files.

Risk: Using an unpinned CLI release such as @latest can introduce unexpected changes.

Mitigation: Use a reviewed, fixed CLI version for repeatable workflows.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-x-twitter)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Guidance]

**Output Format:** [Structured SocialDataX data returned as JSON and summarized in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research; paginated results may require continuation tokens.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
