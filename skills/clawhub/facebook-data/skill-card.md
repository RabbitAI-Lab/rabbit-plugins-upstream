## Description:

Facebook pages, posts, groups, Marketplace listings, and the Ad Library for agents — no Facebook app, review, or login of yours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research teams can query Facebook pages, posts, groups, Marketplace listings, and ads for social and creator intelligence, market research, monitoring, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests are paid, and searches are disclosed to superagnt.

Mitigation: Keep searches within the intended task and review the provider's data handling and pricing before use.

Risk: The SUPERAGNT_API_KEY is a bearer credential.

Mitigation: Store the key securely and avoid exposing it in logs, shared output, or source control.

Risk: The documented curl examples contain HTML-escaped quotes that may prevent them from working as written.

Mitigation: Correct the escaped quotes before running the examples.

## Reference(s):

- [Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Facebook Data MCP server](https://mcp.superagnt.com/mcp/facebook)
- [Facebook Data installation guide](https://www.superagnt.com/install?facet=facebook)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with curl examples; API results are returned as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint-specific request parameters and JSON response fields vary by operation.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
