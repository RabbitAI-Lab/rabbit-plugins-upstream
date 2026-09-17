## Description:

Use this skill for WorkOS requests to read, create, update, and delete data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage WorkOS users, organizations, and organization memberships from an agent session through OOMOL-brokered WorkOS access. It supports read actions plus confirmed write and destructive actions for WorkOS administration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes direct execution of a remote installer for the oo CLI.

Mitigation: Verify the oo CLI source and prefer a pinned or otherwise verified installation path before installing.

Risk: The skill can create, update, deactivate, and reactivate WorkOS resources.

Mitigation: Confirm exact targets, schemas, payloads, and intended effects with the user before write or destructive actions.

Risk: WorkOS access is brokered through OOMOL rather than direct user-managed API credentials.

Mitigation: Install and use the skill only when OOMOL is a trusted broker for the target WorkOS environment.

## Reference(s):

- [WorkOS homepage](https://workos.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-workos)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON data and execution metadata when run with the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
