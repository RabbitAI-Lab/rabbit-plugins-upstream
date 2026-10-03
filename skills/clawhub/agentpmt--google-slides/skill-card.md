## Description:

Google Slides lets an agent create, edit, search, style, and manage Google Slides presentations through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate Google Slides workflows, including creating decks, adding slides and page elements, filling templates, styling content, searching presentations, and generating thumbnails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search, read, create, edit, delete, and run raw update operations on accessible Google Slides presentations.

Mitigation: Use least-privilege Google access, verify presentation and object IDs before destructive actions, and keep backups for important decks.

Risk: Raw batch update requests can heavily alter presentations without built-in confirmation safeguards.

Mitigation: Review generated request payloads before execution and prefer scoped, named actions when they satisfy the task.

Risk: Credential or payment secrets could be exposed if included in prompts or logs.

Mitigation: Follow the setup skill for credential handling and avoid placing account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.

Risk: Floating setup installs can change over time.

Mitigation: Prefer pinned or reviewed setup-skill versions before deployment.

## Reference(s):

- [Generated action schema](artifact/schema.md)
- [Google Slides marketplace page](https://www.agentpmt.com/marketplace/google-slides)
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/google-slides)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [AgentPMT overview](https://clawhub.ai/agentpmt/what-is-agentpmt)
- [AgentPMT main MCP server](https://api.agentpmt.com/mcp/)
- [AgentPMT REST invoke endpoint](https://api.agentpmt.com/products/purchase)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses are JSON; thumbnail URLs expire after approximately 30 minutes.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
