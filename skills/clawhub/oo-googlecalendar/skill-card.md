## Description:

Operates Google Calendar through an OOMOL-connected account to read, create, update, and delete calendar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting users with Google Calendar use this skill to inspect live connector schemas, read calendar data, and perform confirmed write or destructive operations through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include a remote installer pattern that can execute local code.

Mitigation: Install only if OOMOL is trusted; prefer a versioned package or verify downloaded installer contents before execution.

Risk: Write and destructive Google Calendar actions can modify or remove calendar data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Google Calendar homepage](https://workspace.google.com/products/calendar/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Google Calendar connector actions through the oo CLI and return JSON responses from the connector.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
