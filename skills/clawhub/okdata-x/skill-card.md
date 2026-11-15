## Description:

读取 X（推特）的公开帖子、账号、回复、引用和趋势数据，供 AI agent 查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to search public X posts, inspect posts and account activity, and retrieve replies, trends, and related public data through okdata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the required OKDATA_API_KEY sends the key to api.okdata.online when making requests.

Mitigation: Only configure the key if you trust the service; keep it in the OKDATA_API_KEY environment variable and do not paste it into chat.

Risk: API calls incur per-call charges.

Mitigation: Estimate and communicate expected costs before calling, and set max_price for MCP calls.

## Reference(s):

- [okdata X API documentation](https://okdata.online/zh/apis/x/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-x)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON data with concise natural-language summaries and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by API endpoint and page; API calls may incur per-call charges.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
