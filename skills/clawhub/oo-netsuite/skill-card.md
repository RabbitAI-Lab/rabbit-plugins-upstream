## Description:

NetSuite (netsuite.com). Use this skill for NetSuite requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to inspect NetSuite schemas and run connector actions for records and SuiteQL through the oo CLI. It supports read workflows and user-confirmed create or update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts, which creates local execution risk.

Mitigation: Review the oo CLI installation source before installing and prefer a verified, version-pinned installer or package-manager flow.

Risk: Create and update actions can change NetSuite records.

Mitigation: Use the skill only with a NetSuite account authorized for the target records, and require confirmation of the exact payload and expected effect before write actions.

Risk: Incorrect payloads or stale assumptions about action fields could produce failed or unintended NetSuite operations.

Mitigation: Inspect the live connector schema for the chosen action before building each payload.

## Reference(s):

- [ClawHub NetSuite skill page](https://clawhub.ai/oomol/skills/oo-netsuite)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [NetSuite homepage](https://www.netsuite.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use oo connector schema and oo connector run; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
