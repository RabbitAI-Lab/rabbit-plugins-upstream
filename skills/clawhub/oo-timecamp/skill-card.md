## Description:

TimeCamp (timecamp.com). Use this skill for TimeCamp requests that read, create, or update TimeCamp data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users with an OOMOL-connected TimeCamp account use this skill to inspect TimeCamp account data and manage time tracking workflows. It supports reading users, tasks, timer status, and time entries, plus creating or updating time entries and starting or stopping timers after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may run an unverified internet installer directly in a shell.

Mitigation: Prefer the official install guide or a signed/package-manager install path, inspect and verify any downloaded installer before running it, and avoid elevated shells.

Risk: TimeCamp write actions can create or update time entries and start or stop timers.

Mitigation: Confirm the exact payload and expected effect with the user before executing any write action.

Risk: OOMOL mediates TimeCamp actions for the connected account.

Mitigation: Install only when that mediation is acceptable for the account and workflow being used.

## Reference(s):

- [TimeCamp homepage](https://www.timecamp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timecamp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; TimeCamp write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
