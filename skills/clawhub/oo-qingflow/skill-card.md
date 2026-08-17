## Description:

轻流 is a Qingflow connector skill for reading and changing Qingflow workspace, business record, workflow, comment, and log data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Qingflow workspace data and business records through an OOMOL-connected account, including discovery, record updates, workflow actions, comments, change logs, and async operation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can expose Qingflow business data available to the connected OOMOL account.

Mitigation: Install only when Codex is intended to access Qingflow, and treat read actions as business-data access.

Risk: Write actions can create, update, reassign, process, or comment on business records.

Mitigation: Require confirmation of the exact payload and expected effect before running write actions.

Risk: Destructive rollback actions can overwrite or reverse workflow state.

Mitigation: Confirm the target record and rollback destination, and require explicit approval before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qingflow)
- [轻流 homepage](https://qingflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL app connections](https://console.oomol.com/app-connections?provider=qingflow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
