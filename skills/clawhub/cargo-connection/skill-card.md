## Description:

Connect Cargo to external systems by guiding connector authentication, integration catalog discovery, and lookup of connector UUIDs and action slugs for workflow nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo connectors, inspect supported integrations, resolve action schemas, and prepare connector references for Cargo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide persistent connector changes, including creating, updating, or removing business integrations.

Mitigation: Confirm the active Cargo workspace before write operations and require explicit approval before connector removal.

Risk: Connector setup and updates may involve credentials or API tokens.

Mitigation: Avoid pasting real API keys directly in shell commands and prefer a trusted, pinned CLI installation path.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Connector examples](references/examples/connectors.md)
- [Integration examples](references/examples/integrations.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI commands generally emit JSON responses and may require a signed-in Cargo workspace.]

## Skill Version(s):

1.4.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
