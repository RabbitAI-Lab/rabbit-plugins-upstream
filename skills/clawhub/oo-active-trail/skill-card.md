## Description:

ActiveTrail lets agents manage ActiveTrail contacts, groups, group membership, and account balance through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage ActiveTrail contact and group data through an OOMOL-connected account. It supports read, write, and destructive actions with confirmation requirements for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Avoid pipe-to-shell installation unless the OOMOL installer source has been independently trusted and verified; prefer a pinned, signed, or checksum-verified oo CLI installation path.

Risk: Write and destructive ActiveTrail actions can modify or delete contacts, groups, or group membership.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive connector actions.

## Reference(s):

- [ActiveTrail homepage](https://www.activetrail.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-active-trail)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
