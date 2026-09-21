## Description:

Kingdee (kingdee.com). Use this skill for ANY Kingdee request — reading, creating, updating, and deleting data. Whenever a task involves Kingdee, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to let an agent inspect Kingdee Galaxy Enterprise schemas and run approved Kingdee connector actions for reading, creating, updating, submitting, auditing, allocating, pushing, deleting, and reporting on business records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change, overwrite, approve, reverse, allocate, push, or delete Kingdee ERP records.

Mitigation: Require explicit user review and approval of every write, destructive, or proxy payload before execution, including the target records and expected business effect.

Risk: The first-time setup section includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Install the oo CLI through a verified, user-controlled process and review installer contents before running them.

Risk: The skill grants an agent mediated access to Kingdee business data through a connected account.

Mitigation: Use a least-privilege Kingdee account and connect only the scopes needed for the intended workflow.

Risk: Timed-out, interrupted, or partial-success writes may already have changed records.

Mitigation: Reconcile current Kingdee state with known record identifiers before retrying or reporting completion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kingdee)
- [Kingdee homepage](https://www.kingdee.com/cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Proxy reference](references/proxy-reference.md)
- [Official third-party authorization setup](https://open.kingdee.com/K3Cloud/Open/ApiCenterReportDetail.aspx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Kingdee action names, oo CLI commands, JSON request payloads, result interpretation guidance, and approval prompts for write or destructive operations.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
