## Description:

Skyvern helps agents operate Skyvern browser automation through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start, inspect, list, and cancel Skyvern browser automation runs from an agent session while relying on OOMOL-managed account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct an agent to run unverified remote installer scripts for the oo CLI.

Mitigation: Install only from trusted OOMOL sources, manually review the installer first, or use a safer verified installation method before enabling the skill.

Risk: The skill's action scoping is broader than ideal for operating Skyvern.

Mitigation: Require explicit user approval before starting or canceling Skyvern runs, and inspect the live action schema before constructing any payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skyvern)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skyvern homepage](https://www.skyvern.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on an installed, authenticated oo CLI and an OOMOL-connected Skyvern account.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
