## Description:

Sif operates Amazon market analysis through an OOMOL-connected account using the oo CLI and live Sif connector schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and analysts use this skill to discover Sif Amazon analysis tools, inspect live action schemas, and run market, keyword, competitor, ASIN, demand, trend, and opportunity analyses through OOMOL-connected Sif access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts without an in-skill checksum or signature verification step.

Mitigation: Review the installer source and prefer a signed, versioned, checksum-verified installation path before running installer commands, especially from sensitive or privileged shells.

Risk: Sif actions may consume Sif points or encounter billing stops such as HTTP 402 or OOMOL_INSUFFICIENT_CREDIT.

Mitigation: Inspect the live action schema before execution and confirm expected cost-sensitive requests with the user when needed.

## Reference(s):

- [Sif homepage](https://www.sif.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include Sif connector JSON data and execution metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
