## Description:

Tanium enables an agent to inspect connector schemas and execute GraphQL documents against a connected Tanium Gateway endpoint through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security operators use this skill to work with Tanium data through an existing OOMOL-connected Tanium account. It supports schema-first command construction before running GraphQL operations against Tanium Gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw GraphQL action may change enterprise security data if a mutation or ambiguous operation is executed.

Mitigation: Use a Tanium/OOMOL account limited to the intended read-only scope and require explicit approval before any GraphQL mutation or ambiguous operation.

Risk: The first-time setup section includes remote installer commands that pipe downloaded content directly to a shell.

Mitigation: Avoid the pipe-to-shell installer path unless the installer source and integrity have been independently verified.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Tanium homepage](https://www.tanium.com)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tanium)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first oo CLI commands and JSON responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
