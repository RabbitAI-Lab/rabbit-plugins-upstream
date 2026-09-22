## Description:

Track how a brand shows up in ChatGPT and Google AI Overviews answers, and act on the findings, through Shruwd's MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ilpr](https://clawhub.ai/user/ilpr)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, SEO, and brand teams use this skill to connect an agent to Shruwd's MCP server, set up brands, track prompts and competitors, run AI-search visibility measurements, and review results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Shruwd API key that acts with the user's Shruwd workspace role.

Mitigation: Install only for agents that should access the workspace, keep SHRUWD_API_KEY scoped to the intended account, and review actions before approval.

Risk: Agent actions can create brands, add prompts or competitors, run measurements, or archive items in Shruwd.

Mitigation: Review proposed workspace changes before execution, especially actions that affect brand tracking setup or measurement cycles.

## Reference(s):

- [Shruwd homepage](https://shruwd.io)
- [Shruwd docs](https://shruwd.io/docs)
- [Shruwd machine-readable docs](https://shruwd.io/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with shell commands and API-backed MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHRUWD_API_KEY for Shruwd workspace access; SHRUWD_API_URL is optional and defaults to https://shruwd.io/api/v1.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
