## Description:

Search Zhihu's public questions, answers, and articles and retrieve answers for a question through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can search Zhihu's public questions, answers, and articles or retrieve the leading answers to a question using okdata. The skill supports public-data research without Zhihu login or cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to an external API using an API key, and calls may incur per-request charges.

Mitigation: Use the API only if you trust the provider, keep the key in the OKDATA_API_KEY environment variable rather than chat, review expected cost before calling, and set max_price where supported.

## Reference(s):

- [okdata Zhihu API documentation and pricing](https://okdata.online/zh/apis/zhihu/)
- [okdata remote MCP endpoint](https://api.okdata.online/mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Analysis]

**Output Format:** [Zhihu search results and answer data presented as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public data; calls may incur per-request charges.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
