## Description:

Everhour (everhour.com). Use this skill for ANY Everhour request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Everhour data through an OOMOL-connected account, including reading projects, tasks, users, timers, and time records. It also supports creating time records and starting or stopping timers after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer before use and prefer a verified, versioned, or package-manager installation path for the oo CLI.

Risk: Write actions can create time records or start and stop Everhour timers.

Mitigation: Confirm the exact action, payload, and expected Everhour state change with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-everhour)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Everhour homepage](https://everhour.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use live connector schemas and return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
