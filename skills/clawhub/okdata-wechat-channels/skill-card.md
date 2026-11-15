## Description:

Provides AI agents with read-only access to public WeChat Channels videos, accounts, comments, and livestream replays through the Okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT

## Use Case:

External users can search public WeChat Channels videos and accounts, retrieve post details and engagement, read comments and replies, and inspect livestream replays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send the query or identifiers needed for retrieval to the external Okdata API.

Mitigation: Use the service only if you trust it, and limit requests to the public data needed for the task.

Risk: API calls are billed per request, so multi-step searches can add up.

Mitigation: Estimate the number and cost of calls first and set a max_price for each call.

Risk: The API key grants access to the account's paid API service.

Mitigation: Store the key in the OKDATA_API_KEY environment variable and do not paste it into chat.

Risk: The security review had medium confidence and was partial because some local references could not be resolved.

Mitigation: Review the skill and its configured API service before use, especially before sending sensitive query data.

## Reference(s):

- [Okdata WeChat Channels API documentation](https://okdata.online/zh/apis/wechat_channels/)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text summaries and structured Markdown of retrieved public video, account, engagement, comment, and replay data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on public availability; some metrics may be unavailable or time-sensitive. Video media URLs may be encrypted.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
