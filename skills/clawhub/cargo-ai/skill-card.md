## Description:

Guides agents through creating and configuring Cargo AI agents, attaching knowledge, connecting MCP servers, managing memories, and deploying releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to configure Cargo AI agents, connect them to knowledge and MCP tools, manage agent memories, and deploy releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Replacing agent connection settings with empty arrays can remove unrelated tools and knowledge sources from an existing agent.

Mitigation: Preserve and review the current agent configuration before changing or deploying a release; do not copy empty-array connection examples unchanged.

Risk: Operations can affect the active workspace, including file uploads or deletions.

Mitigation: Confirm the target workspace and explicitly authorize uploads or deletions before running commands.

Risk: The external CLI and sibling skills were not inspected in this release review.

Mitigation: Use a reviewed CLI version with limited permissions and review deployment changes before using the skill on an existing agent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-ai)
- [Cargo Skills project homepage (listed in skill metadata)](https://github.com/getcargohq/cargo-skills)
- [Agent examples](references/examples/agents.md)
- [MCP server examples](references/examples/mcp-servers.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with shell command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that create, update, deploy, or remove Cargo AI resources.]

## Skill Version(s):

2.8.2 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
