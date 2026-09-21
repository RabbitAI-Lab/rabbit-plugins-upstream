## Description:

Use the BitsWeave MCP server to read shared project context and save durable work for other agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsweave](https://clawhub.ai/user/bitsweave)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to read shared BitsWeave project context before making changes and to save durable findings, decisions, tasks, and documents for later agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project details may be saved to an external BitsWeave service, which can matter for private repositories or sensitive business work.

Mitigation: Review what the agent saves in BitsWeave and avoid storing sensitive or confidential details unless the service is approved for that work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bitsweave/skills/bitsweave)
- [BitsWeave MCP Endpoint](https://bitsweave.com/api/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Text, Markdown]

**Output Format:** [Markdown instructions and MCP tool-mediated text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save shared project context to the BitsWeave external service through OAuth-authenticated MCP tools.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
