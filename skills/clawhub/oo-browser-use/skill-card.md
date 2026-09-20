## Description:

Browser Use operates Browser Use Cloud through an OOMOL-connected account using the oo CLI for browser automation tasks, session inspection, session control, and billing checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run and inspect Browser Use Cloud automation through an OOMOL-connected account, including session and task management, progress review, and billing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the CLI installation path first and prefer an official package manager, pinned release, or verified installer before running setup commands.

Risk: Write and destructive actions can change Browser Use Cloud state or stop active sessions.

Mitigation: Confirm the exact payload, target session, and expected effect with the user before approving write or stop-session actions.

## Reference(s):

- [Browser Use homepage](https://browser-use.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Browser Use skill page](https://clawhub.ai/oomol/skills/oo-browser-use)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes action names, schema-inspection commands, JSON payload guidance, and safety confirmation guidance for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
