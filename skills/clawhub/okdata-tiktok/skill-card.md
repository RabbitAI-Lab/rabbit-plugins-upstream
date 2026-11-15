## Description:

Fetches public TikTok video, account, comment, advertising, and TikTok Shop data through the Okdata API for market and product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill for overseas market and product research, including searching TikTok videos and accounts, reviewing public comments, comparing ads, and checking TikTok Shop products and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send queries or content identifiers to the external Okdata API, and the skill requires an API key.

Mitigation: Review and trust the service before use, avoid sending sensitive information, and keep the API key in the OKDATA_API_KEY environment variable rather than sharing it in conversation.

Risk: API calls are paid, so multi-page research can accumulate charges.

Mitigation: Estimate the number and cost of calls before using the API and set an appropriate max_price for calls.

## Reference(s):

- [Okdata TikTok API documentation](https://okdata.online/zh/apis/tiktok/)
- [Okdata remote MCP endpoint](https://api.okdata.online/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Text or Markdown summaries and research findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on publicly available TikTok data and the selected API calls.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
