## Description:

Remoet helps agents search an open tech job board, identify companies that match a user's stack, and maintain an ongoing feed of relevant roles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[remoet](https://clawhub.ai/user/remoet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and job seekers use this skill to search Remoet's open tech job catalogue, discover companies that match their stack, and manage a curated job-search feed through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to Remoet as a hosted job-search service and may involve profile or CV data when account features are used.

Mitigation: Start keyless for public search, add an API key or OAuth only for account features, and avoid sending full CV or profile details until comfortable with Remoet handling that data.

Risk: Account actions can change profile visibility, submit internal applications, delete saved profile items, or bulk-star companies.

Mitigation: Confirm with the user before profile visibility changes, internal applications, deletions, or bulk starring.

Risk: Most scraped jobs require the user to apply on the employer's site rather than through Remoet.

Mitigation: For external applications, return the employer application URL and make clear that the user completes the application outside Remoet.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/remoet/skills/remoet)
- [ClawHub Publisher Profile](https://clawhub.ai/user/remoet)
- [Remoet Homepage](https://remoet.dev)
- [Remoet Agent Onboarding](https://remoet.dev/onboarding?mode=agent&utm_source=clawhub)
- [Remoet Agent Settings](https://remoet.dev/agents)
- [Remoet MCP Server](https://api.remoet.dev/mcp)
- [Remoet OAuth MCP Server](https://api.remoet.dev/mcp/oauth)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an optional REMOET_API_KEY for account features; public job search and company lookup can run keyless.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
