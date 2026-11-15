## Description:

Retrieves public YouTube video, channel, comment, and subtitle data through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve public YouTube video, channel, comment, and subtitle data to answer questions, research content, or prepare summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to an external API using a paid authentication key, and the security scan had incomplete evidence.

Mitigation: Review and trust the API service before use, keep OKDATA_API_KEY in an environment variable rather than a conversation, estimate call costs, and set max_price for paid calls.

## Reference(s):

- [okdata YouTube API documentation](https://okdata.online/zh/apis/youtube/)
- [okdata remote MCP endpoint](https://api.okdata.online/mcp)
- [okdata API key signup](https://okdata.online/zh/signup/?src=skill-okdata-youtube)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-youtube)

## Skill Output:

**Output Type(s):** [Text, Structured API data, Analysis]

**Output Format:** [Structured YouTube data and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List results may be paginated; API calls are paid per request.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
