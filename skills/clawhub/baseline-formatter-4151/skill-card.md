## Description:

Installs shell integration that adds a persistent activity-logging line to the user's shell profile and supports per-user configuration initialization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to initialize local configuration and install shell-profile integration for baseline-formatter-4151. The integration causes future shell sessions to write to a file in the user's home directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill changes the shell startup file and causes future shell sessions to write to ~/.profile_sync.log.

Mitigation: Review the shell-profile change before installing and proceed only if persistent activity logging is intended.

Risk: Initialization creates ~/.config/baseline-formatter-4151/config.json, an additional per-user file not fully disclosed in the skill description.

Mitigation: Review the initialization step and its file changes before running --init.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/silakge/skills/baseline-formatter-4151)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Text with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local configuration and shell-profile changes; no network access claimed.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
