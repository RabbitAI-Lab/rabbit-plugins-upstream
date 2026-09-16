## Description:

StealthGPT helps agents operate StealthGPT through an OOMOL-connected account for AI-text detection, text generation, text humanization, and balance lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to call StealthGPT actions through the OOMOL `oo` CLI after the account and connector are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installer commands.

Mitigation: Review the OOMOL CLI setup and prefer official, version-pinned, signed, or checksum-verified installation steps before connecting credentials.

Risk: The skill routes StealthGPT use through OOMOL as the account connector.

Mitigation: Install only if OOMOL is an acceptable connector for the target StealthGPT account and billing workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stealthgpt)
- [StealthGPT homepage](https://www.stealthgpt.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
