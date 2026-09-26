## Description:

Helps agents discover and call MCP tools through compact listings and manage skill catalogs across agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find and call configured MCP tools without loading full tool catalogs, and to organize skills across agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a package introduces supply-chain risk.

Mitigation: Verify the PyPI package and source before installation, and consider pinning a known version for production use.

Risk: Mediating tool discovery can also allow calls to configured MCP tools.

Mitigation: Review the tool and its parameters before making a call.

Risk: Skill synchronization may change agent skill folders and leave persistent configuration.

Mitigation: Preview synchronization with dry-run modes and review persistent configuration files when uninstalling.

## Reference(s):

- [Mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool listings can omit upstream tools in compact mode; they remain callable.]

## Skill Version(s):

1.0.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
