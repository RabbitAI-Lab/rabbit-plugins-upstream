## Description:

Guides an agent in using RockDesk's `rds` command line to inspect and operate an authorized remote computer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockdesk-io](https://clawhub.ai/user/rockdesk-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect to authorized RockDesk devices for remote shell, file, clipboard, and graphical interface tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad requests to operate another machine can activate remote-control guidance.

Mitigation: Check the intended machine and action before running commands.

Risk: Remote shell, file, clipboard, and device controls can expose data or change remote state.

Mitigation: Use only machines you are authorized to control, confirm destructive or irreversible actions, and keep clipboard history private.

Risk: A background service may continue running after logout or restart.

Mitigation: Review whether persistent access is intended before enabling the service.

## Reference(s):

- [RockDesk download page](https://rockdesk.io/#download)
- [RockDesk release notes](https://rockdesk.io/rockd-latest.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Operational guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
