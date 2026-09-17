## Description:

GoSquared (gosquared.com). Use this skill for ANY GoSquared request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate GoSquared through an OOMOL-connected account, including realtime Now overviews, visitor time series, token authorization checks, and Trends aggregate metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer source before use, prefer a pinned, signed, or checksum-verified installation path, and avoid running setup from an elevated shell.

Risk: The skill relies on an OOMOL-connected GoSquared account, so incorrect account or scope configuration can affect what project data the agent can read.

Mitigation: Inspect token authorization with get_token_info and confirm the intended GoSquared connection before using project data for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gosquared)
- [GoSquared homepage](https://www.gosquared.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from GoSquared connector actions when commands are executed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
