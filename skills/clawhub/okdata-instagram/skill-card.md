## Description:

Public Instagram data through okdata: accounts, posts, comment replies, hashtags. 8 endpoints, $0.002–$0.004 a call. Use when a task needs Instagram data. 通过 okdata 取Instagram公开数据：账号、帖子、评论回复、话题。8 个接口，每次 $0.002–$0.004。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve public Instagram account, post, comment, hashtag, and reel transcript data through okdata for analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Instagram lookup details to an external API service, and scanner coverage is incomplete.

Mitigation: Use okdata only if you trust the service, review the identifiers being sent, and avoid including sensitive information.

Risk: Endpoint calls are paid, and retrieving additional pages requires additional calls.

Mitigation: Before the first paid call, state the endpoint, number of calls, and maximum cost; fetch more pages only when needed.

## Reference(s):

- [Instagram API documentation](https://okdata.online/apis/instagram/?src=skill-okdata-instagram)
- [okdata agent setup guide](https://okdata.online/agents.md)
- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-instagram)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text responses with endpoint reference tables, JSON request examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each API call returns one page of data; additional pages require separate calls.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
