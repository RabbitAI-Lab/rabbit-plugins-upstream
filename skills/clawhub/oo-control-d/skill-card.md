## Description:

Control D helps agents operate Control D through an OOMOL-connected account to read, create, update, and delete profile DNS data via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Control D profiles, profile rules, service discovery, and troubleshooting through an OOMOL-connected Control D account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run remote installer scripts directly in a shell.

Mitigation: Review the installer step before use and prefer documented, verifiable package-manager or checksum-verified installation steps.

Risk: Profile rule actions can delete, replace, or overwrite Control D DNS configuration.

Mitigation: Confirm the exact profile, rule targets, and payload with the user before allowing destructive Control D actions.

## Reference(s):

- [ClawHub Control D skill page](https://clawhub.ai/oomol/skills/oo-control-d)
- [Control D homepage](https://controld.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
