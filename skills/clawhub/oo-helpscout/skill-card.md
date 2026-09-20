## Description:

Help Scout lets an agent read and manage Help Scout conversations, customers, inboxes, users, tags, workflows, saved replies, threads, and custom fields through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to handle Help Scout support data from an agent session, including listing records, creating customers or conversations, replying, adding notes, updating status, assigning conversations, managing tags, and running manual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote installer for the oo CLI.

Mitigation: Review the installer source or use a trusted installation method before setup.

Risk: The skill can perform account-changing Help Scout actions, including writes, workflow runs, tag changes, status changes, assignments, snoozes, and custom-field updates.

Mitigation: Require explicit user confirmation of the target, payload, and intended effect before any write or destructive action.

## Reference(s):

- [Help Scout homepage](https://www.helpscout.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-helpscout)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; executed oo CLI actions return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can be run directly; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
