## Description:

Helps agents operate Kraken.io through the OOMOL oo CLI by inspecting action schemas, checking account status, and optimizing images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Kraken.io account-status and image-optimization actions through an OOMOL-connected account, after inspecting the live action schema and confirming payloads for actions that upload or process images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute unreviewed code during first-time setup.

Mitigation: Prefer a verified package or inspect and verify the installer before running it.

Risk: Image optimization may upload private image content, process it through Kraken.io, or consume account quota.

Mitigation: Confirm the exact optimize_image payload and user intent before running the action.

Risk: Using the skill relies on OOMOL mediating Kraken.io account access.

Mitigation: Use the skill only when the user is comfortable with OOMOL-connected account access for Kraken.io.

## Reference(s):

- [ClawHub Kraken.io Skill](https://clawhub.ai/oomol/skills/oo-kraken-io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Kraken.io](https://kraken.io)
- [Kraken.io Icon](https://static.oomol.com/logo/third-party/Kraken.io.svg)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector JSON data and execution identifiers returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
