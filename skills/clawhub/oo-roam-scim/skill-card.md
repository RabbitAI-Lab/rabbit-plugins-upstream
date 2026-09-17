## Description:

Roam SCIM (ro.am) supports reading, creating, updating, and deleting data through the OOMOL-connected Roam SCIM service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and administrators use this skill to operate Roam SCIM user and group lifecycle workflows through the OOMOL `oo` CLI connector, including read, create, update, replace, archive, and delete/archive actions. It is intended for schema-first SCIM administration where state-changing actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's first-time setup includes remote installer snippets for the oo CLI, and the security summary flags direct execution of unverified remote installer scripts as suspicious.

Mitigation: Use a verified, signed, or package-manager based oo CLI installation path before executing Roam SCIM operations.

Risk: Roam SCIM write and destructive actions can create, replace, archive, delete, or otherwise modify users and groups.

Mitigation: Fetch the live action schema first, confirm the exact target, payload, and effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [Roam SCIM homepage](https://ro.am)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub Roam SCIM skill page](https://clawhub.ai/oomol/skills/oo-roam-scim)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke `oo connector schema` and `oo connector run` commands that return JSON responses from Roam SCIM actions.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
