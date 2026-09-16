## Description:

AppDrag operates the AppDrag connector through an OOMOL-connected account to inspect action schemas and execute AppDrag Cloud Backend API functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run AppDrag Cloud Backend API functions through the OOMOL `oo` CLI after checking the live connector schema. It is intended for AppDrag tasks where the agent should use the managed connector instead of calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad AppDrag backend function execution through an authenticated OOMOL-connected account.

Mitigation: Require explicit user confirmation before every `execute_function` call, especially non-GET methods or functions that could modify or delete data.

Risk: The first-time setup instructions include pipe-to-shell installer commands.

Mitigation: Avoid running installer commands unless the installer source and integrity have been independently verified.

## Reference(s):

- [AppDrag homepage](https://appdrag.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appdrag)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
