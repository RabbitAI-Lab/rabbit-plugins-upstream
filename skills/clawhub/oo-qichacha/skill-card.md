## Description:

Qichacha (openapi.qcc.com). Use this skill for ANY Qichacha request - searching and reading data. Whenever a task involves Qichacha, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business analysts use this skill to query Qichacha company data through an OOMOL-connected account. It supports read-only workflows for historical outbound investments, exit details, shareholder records, and subscribed contribution details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup payloads may be sent to the OOMOL/Qichacha connector through the user's connected account.

Mitigation: Use the skill only when Qichacha lookup through that account is intended, and avoid including unnecessary sensitive information in payloads.

Risk: First-time setup may require installing the oo CLI and connecting Qichacha credentials.

Mitigation: Run setup only after an auth or connection failure, and follow the user's approved credential and software installation process.

## Reference(s):

- [ClawHub Qichacha skill page](https://clawhub.ai/oomol/skills/oo-qichacha)
- [Qichacha OpenAPI](https://openapi.qcc.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON; action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
