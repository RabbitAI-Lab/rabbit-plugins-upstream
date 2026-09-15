## Description:

ExpoFP lets agents use OOMOL's oo CLI to inspect ExpoFP connector schemas and read, create, update, or delete ExpoFP exhibitor data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams with connected OOMOL and ExpoFP accounts use this skill to manage ExpoFP expos and exhibitors through connector actions. It supports schema inspection, read actions, and user-confirmed write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands executed directly in a shell.

Mitigation: Review the OOMOL CLI distribution path before installation and prefer a verified, pinned, or package-manager installation method when available.

Risk: The skill can create, update, and delete ExpoFP exhibitor records.

Mitigation: Inspect the live connector schema before payload construction, confirm exact write payloads and effects with the user, and require explicit approval before destructive deletion.

## Reference(s):

- [ExpoFP homepage](https://expofp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ExpoFP skill page](https://clawhub.ai/oomol/skills/oo-expofp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes connector action names, schema-inspection commands, JSON payload guidance, and approval requirements for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
