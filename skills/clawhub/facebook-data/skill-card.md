## Description:

Helps agents query Facebook pages, posts, groups, ads, and marketplace data through the superagnt API for brand and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research analysts use this skill to retrieve Facebook content and marketplace signals for social listening, competitive research, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facebook queries and the API credential are sent to superagnt.

Mitigation: Use only with an approved account and data-sharing arrangement; protect the credential and avoid exposing it in logs or responses.

Risk: People, seller, group, marketplace, ad, and media endpoints can collect sensitive or personal information without built-in consent boundaries.

Mitigation: Limit requests to authorized purposes and necessary data; review privacy requirements and Facebook platform rules before collection or redistribution.

Risk: Proxy-backed and scraping-described workflows may exceed acceptable platform use.

Mitigation: Review endpoint parameters and platform terms before use; avoid proxy or collection settings that circumvent access restrictions.

## Reference(s):

- [Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [superagnt app and API keys](https://superagnt.com/r/ch-facebook-data-key)
- [Facebook Data ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)
- [Facebook MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API access requires a superagnt credential and may consume credits.]

## Skill Version(s):

2.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
