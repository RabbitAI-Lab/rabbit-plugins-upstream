## Description:

mcptoon helps agents compress MCP tool discovery, inspect and call MCP tools through a CLI, and manage shared skill catalogs across agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use mcptoon to reduce large MCP tool catalogs into compact manifests, inspect schemas when needed, call tools, and synchronize skill folders across supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill sync, add, remove, and tombstone workflows can change local skill folders.

Mitigation: Use dry-run for sync operations and review affected paths before add, remove, or tombstone commands.

Risk: Installing or upgrading a CLI from an unexpected package source could introduce untrusted code.

Mitigation: Verify the PyPI package and source before installing or upgrading mcptoon.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recommendations and operational guidance for using the mcptoon CLI; it does not itself execute tool calls unless the agent chooses to run the suggested commands.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
