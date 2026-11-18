## Description:

Facebook pages, posts, groups, Marketplace listings, and the Ad Library for agents — no Facebook app, review, or login of yours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, research, and social listening teams can use this skill to gather Facebook page and group content, Marketplace listings, and ad information for monitoring, creator research, alerts, and dashboards. Developers can connect those results to downstream analytics and AI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan noted people search beyond the skill's stated Facebook content scope and a possible mismatch involving a credit-checking operation.

Mitigation: Review the documented operations and decide whether those capabilities fit the intended use before enabling the skill.

Risk: The skill sends an API key to an external service and includes a credit-checking operation.

Mitigation: Use the service only if trusted, protect the API key, and check account credit usage.

## Reference(s):

- [Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Facebook Data API key and account](https://superagnt.com/r/ch-facebook-data-key)
- [Facebook Data MCP setup](https://www.superagnt.com/install?facet=facebook)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON data from Facebook surfaces, optionally summarized for downstream research and analytics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live API results depend on service availability and account credits.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
