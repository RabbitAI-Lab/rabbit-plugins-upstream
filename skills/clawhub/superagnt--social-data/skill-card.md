## Description:

Provides agents with structured social-platform data, web scraping, SEO research, and hosted webhook receiving through Superagnt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve social, web, and SEO data and to receive third-party webhook events through Superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Social identifiers, URLs, keywords, and model prompts are sent to Superagnt.

Mitigation: Avoid sending secrets or regulated data in prompts or scrape targets; review data-sharing suitability before use.

Risk: Hosted webhook URLs may expose incoming events if shared or leaked.

Mitigation: Treat generated webhook URLs as credentials and avoid logging or sharing them unnecessarily.

Risk: Webhook payloads may be unauthenticated or originate from an unexpected sender.

Mitigation: Validate vendor signatures or event origin before allowing agents to take business actions from webhook payloads.

## Reference(s):

- [Social Data ClawHub listing](https://clawhub.ai/superagnt/skills/social-data)
- [Superagnt documentation](https://superagnt.com/r/ch-social-data-docs)
- [Superagnt MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Web API reference](references/web/README.md)
- [SEO API reference](references/seo/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON data]

**Output Format:** [Markdown guidance and shell commands; structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API access requires a Superagnt key and available credits; MCP is an alternative connection.]

## Skill Version(s):

2.0.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
