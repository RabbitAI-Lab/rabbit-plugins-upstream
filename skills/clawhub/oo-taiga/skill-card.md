## Description:

Use this skill to read, create, and update Taiga data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Taiga projects, issues, tasks, and user stories through an OOMOL-connected account. It supports read, create, list, and update workflows while requiring confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can execute downloaded installer scripts from the internet.

Mitigation: Prefer a verified or package-manager installation path, or review the installer before execution.

Risk: Create and update actions can change Taiga project data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Taiga homepage](https://taiga.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-taiga)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
