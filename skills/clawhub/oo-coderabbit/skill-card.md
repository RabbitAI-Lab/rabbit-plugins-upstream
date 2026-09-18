## Description:

CodeRabbit (coderabbit.ai). Use this skill for ANY CodeRabbit request: reading, creating, updating, and deleting data through OOMOL-connected CodeRabbit access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect CodeRabbit schemas and run CodeRabbit organization actions through the oo CLI, including user, role, seat, audit log, and review metrics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that pipe downloaded content directly into a shell.

Mitigation: Prefer official, versioned, and verifiable oo CLI installation instructions before installation.

Risk: The skill can guide broad administrative CodeRabbit operations, including role, seat, and deletion actions.

Mitigation: Confirm the exact organization, target users or roles, intended effect, and payload before running state-changing or destructive actions.

## Reference(s):

- [ClawHub CodeRabbit skill page](https://clawhub.ai/oomol/skills/oo-coderabbit)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [CodeRabbit homepage](https://www.coderabbit.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first command guidance and JSON responses from the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
