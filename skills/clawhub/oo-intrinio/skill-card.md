## Description:

Use this skill to search and read Intrinio data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Intrinio through an OOMOL-connected account for historical stock prices, company lookup, security lookup, and company search tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask users to execute remote installer scripts for the OOMOL CLI.

Mitigation: Review the installer source first, prefer a versioned official installer, and verify any available signature or checksum before execution.

Risk: An agent could attempt first-time setup automatically after a failed command.

Mitigation: Require user review before running installer or authentication setup commands; use normal Intrinio actions directly only after the oo CLI and connection are already configured.

## Reference(s):

- [Intrinio homepage](https://intrinio.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intrinio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal actions are read-oriented Intrinio queries run through the oo CLI; setup guidance is used only after authentication, connection, billing, or missing-command failures.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
