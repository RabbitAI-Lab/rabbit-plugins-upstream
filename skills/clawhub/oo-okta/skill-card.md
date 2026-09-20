## Description:

Okta helps agents read, create, update, and delete Okta users, groups, and group memberships through the OOMOL okta connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, IT administrators, and developers use this skill to inspect and manage Okta users, groups, memberships, and lifecycle actions from an agent workflow. It is intended for OOMOL-connected Okta accounts with user confirmation before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Okta lifecycle operations can change account access, and the security evidence notes that lifecycle_user lacks the confirmation tag used for other mutations.

Mitigation: Require explicit user confirmation for lifecycle_user and all write or destructive Okta operations before execution.

Risk: The skill can operate with broad Okta authority if the connected OOMOL account has excessive permissions.

Mitigation: Use an Okta/OOMOL account scoped only to the administrative tasks intended for this skill.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer verified or package-manager installation of the oo CLI where possible, and review installer commands before running them.

## Reference(s):

- [ClawHub Okta skill page](https://clawhub.ai/oomol/skills/oo-okta)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Okta homepage](https://www.okta.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Okta connector JSON responses containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
