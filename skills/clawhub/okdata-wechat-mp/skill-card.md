## Description:

Retrieves public WeChat Official Account data through the okdata service, including account discovery, articles, metrics, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and AI agents use this skill to find WeChat Official Accounts and retrieve public articles, account details, engagement metrics, and comments for summaries, content research, or competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes requests to the external okdata service, and security scan coverage is incomplete.

Mitigation: Use it only if you trust okdata, keep OKDATA_API_KEY in an environment variable, and review the expected per-call cost before invoking paid endpoints.

## Reference(s):

- [okdata WeChat Official Account API documentation](https://okdata.online/zh/apis/wechat_mp/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-wechat-mp)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [Structured API data (JSON) and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public data; API calls may incur per-request charges.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
