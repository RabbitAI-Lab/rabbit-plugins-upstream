## Description:

TimeCamp helps agents operate TimeCamp through the OOMOL CLI connector for reading account data and managing timers or time entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read TimeCamp account data, inspect tasks and time entries, and create, update, start, or stop time tracking through an OOMOL-connected TimeCamp account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional remote installer command can execute code from the OOMOL CLI installation endpoint.

Mitigation: Review the oo CLI installation path before running the remote installer and install only if comfortable using OOMOL as an intermediary for TimeCamp.

Risk: Write and destructive actions can create, update, stop, or otherwise change TimeCamp timers and time entries.

Mitigation: Confirm the exact target and payload with the user before approving any state-changing TimeCamp action.

## Reference(s):

- [ClawHub TimeCamp skill page](https://clawhub.ai/oomol/skills/oo-timecamp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [TimeCamp homepage](https://www.timecamp.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector responses that include data and an execution ID when actions run.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
