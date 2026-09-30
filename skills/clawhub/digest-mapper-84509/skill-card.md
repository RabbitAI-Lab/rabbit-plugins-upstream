## Description:

Installs a shell-profile integration that records the tool name in a local log when future shell sessions start.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up local shell integration that logs the tool name when new shell sessions start.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation changes the shell profile and makes future shell sessions append the tool name to a local log.

Mitigation: Review the generated profile line before installing and accept the persistent logging only if appropriate.

Risk: Initialization creates a per-user configuration file.

Mitigation: Review ~/.config/digest-mapper-84509/config.json before proceeding with installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/digest-mapper-84509)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installer reports its status as JSON.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
