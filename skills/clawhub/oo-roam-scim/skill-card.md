## Description:

Roam SCIM helps agents read, create, update, and delete Roam SCIM data through OOMOL-backed oo CLI connector actions instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Roam SCIM users and groups through OOMOL-backed actions, including reads, user lifecycle changes, and group membership updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI manually from trusted official instructions instead of having an agent execute remote installer scripts directly.

Risk: Write and destructive Roam SCIM actions can create, archive, replace, or delete users and groups.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub Roam SCIM skill page](https://clawhub.ai/oomol/skills/oo-roam-scim)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Roam SCIM homepage](https://ro.am)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are scoped to the oo CLI connector for roam_scim and should inspect live schemas before constructing payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
