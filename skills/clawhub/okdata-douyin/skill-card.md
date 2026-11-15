## Description:

This skill retrieves public Douyin video, account, comment, trend, and creator data through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to research Douyin videos, accounts, comments, trends, and creator rates for content and influencer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external data service, and requests can include search terms or public profile and comment identifiers.

Mitigation: Use the service only when trusted and needed; do not send secrets or personal information.

Risk: API usage is billed per call, and the security review reports partial coverage.

Mitigation: Check the published prices and estimate call counts before use; review the documented API behavior because the benign scan verdict is not a guarantee of zero risk.

## Reference(s):

- [okdata Douyin API documentation](https://okdata.online/zh/apis/douyin/)
- [okdata remote MCP service](https://api.okdata.online/mcp)
- [okdata account registration](https://okdata.online/zh/signup/?src=skill-okdata-douyin)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Retrieved data summarized as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated; API calls are billed per request according to the published price list.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
