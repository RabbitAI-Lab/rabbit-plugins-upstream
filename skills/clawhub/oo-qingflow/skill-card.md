## Description:

Qingflow lets an agent read, create, update, and delete Qingflow workspace data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to let an agent inspect Qingflow workspace structure and manage business records, workflow actions, comments, reminders, and audit logs through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Qingflow business records and workflow state through write actions.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Rollback actions can remove or overwrite workflow progress on a Qingflow record.

Mitigation: Require explicit user approval for the target record and rollback destination before running destructive actions.

Risk: The agent may have access to connected workspace data after installation.

Mitigation: Install only for workspaces where agent access to Qingflow data is intended, and review sensitive read or audit requests before use.

## Reference(s):

- [ClawHub Qingflow skill page](https://clawhub.ai/oomol/skills/oo-qingflow)
- [Qingflow homepage](https://qingflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confirmation prompts for write or destructive actions; connector responses are JSON.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
