## Description:

ScrapeBadger lets agents retrieve web, social, marketplace, real-estate, and search data through its APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xghostcasper](https://clawhub.ai/user/0xghostcasper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ScrapeBadger to search websites and retrieve public social, marketplace, real-estate, and product information through a single API skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied URLs, queries, or other request data are sent to ScrapeBadger; the security assessment notes that the skill lacks a privacy warning.

Mitigation: Tell users what request data will be sent and confirm they are comfortable sharing it before submitting sensitive information.

Risk: The security scan was partial and could not resolve several local path-like references, so its benign verdict has medium confidence.

Mitigation: Review the skill and its unresolved references before installation or use.

## Reference(s):

- [ScrapeBadger Documentation](https://docs.scrapebadger.com)
- [ScrapeBadger MCP Server](https://mcp.scrapebadger.com/mcp)
- [GitHub Profiles API Reference](https://docs.scrapebadger.com/github/profiles)
- [Brave Search API Overview](https://docs.scrapebadger.com/brave/overview)

## Skill Output:

**Output Type(s):** [API data, JSON, Markdown]

**Output Format:** [Structured endpoint responses, typically JSON; general web pages can be returned as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected endpoint and request; API access requires SCRAPEBADGER_API_KEY.]

## Skill Version(s):

1.10.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
