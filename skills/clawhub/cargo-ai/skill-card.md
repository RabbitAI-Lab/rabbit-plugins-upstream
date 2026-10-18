## Description:

Guides developers in creating, configuring, and deploying Cargo AI agents with knowledge, MCP tools, and memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to manage Cargo AI agents, configure their models and knowledge sources, connect MCP tools, and deploy agent releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change or remove live Cargo resources in the wrong workspace.

Mitigation: Confirm the active workspace with `cargo-ai whoami` and review resource UUIDs before deploying or removing resources.

Risk: API tokens used for authentication or direct API calls may expose privileged access.

Mitigation: Use least-privilege Cargo tokens and protect them when using the direct API workaround.

Risk: Installing the latest CLI without a version pin can change command behavior unexpectedly.

Mitigation: Review and pin the Cargo CLI version before use in controlled environments.

## Reference(s):

- [ClawHub cargo-ai release](https://clawhub.ai/cargo-ai/skills/cargo-ai)
- [Cargo skill homepage (listed in metadata)](https://github.com/getcargohq/cargo-skills)
- [Agent examples](references/examples/agents.md)
- [MCP server examples](references/examples/mcp-servers.md)
- [Cargo CLI response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authenticated Cargo workspace.]

## Skill Version(s):

2.5.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
