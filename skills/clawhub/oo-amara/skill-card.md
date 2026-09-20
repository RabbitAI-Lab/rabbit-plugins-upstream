## Description:

Amara (amara.org). Use this skill for Amara requests including reading, creating, updating, and deleting data through the OOMOL-connected Amara connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage Amara videos, subtitle languages, subtitle versions, notes, URLs, teams, users, and activity through the oo CLI. It supports read operations as well as user-confirmed write and destructive Amara actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup may run a remote oo CLI installer directly in the shell without integrity checks.

Mitigation: Review the installer path before installation and prefer a trusted, versioned source with integrity verification.

Risk: Write and destructive Amara actions can change, remove, or overwrite Amara data.

Mitigation: Confirm the exact action, target, and payload with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Amara homepage](https://amara.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions are run.]

## Skill Version(s):

1.0.4 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
