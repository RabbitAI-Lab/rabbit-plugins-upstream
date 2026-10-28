## Description:

X posts, profiles, followers, and search for agents — audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and research or marketing teams use this skill to search X content, inspect accounts and audiences, and support social listening or creator research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send prompts and analysis text to superagnt, and API use can consume credits.

Mitigation: Review the provider's privacy and pricing terms, share only appropriate data, and monitor credit use.

Risk: The skill uses a bearer API key, which could be exposed if handled carelessly.

Mitigation: Keep SUPERAGNT_API_KEY in a protected environment variable and avoid printing or embedding it in shared commands.

Risk: The documented shell examples may need correction before they run as intended.

Mitigation: Inspect and correct each command, then verify it with a minimal request before relying on larger workflows.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [API key setup](https://superagnt.com/r/ch-x-twitter-data-key)
- [Scoped MCP server](https://mcp.superagnt.com/mcp/x)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/x-twitter-data)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl examples; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API usage may consume credits.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
