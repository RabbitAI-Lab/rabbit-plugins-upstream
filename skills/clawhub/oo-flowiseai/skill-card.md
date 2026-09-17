## Description:

FlowiseAI lets agents operate a connected FlowiseAI account through OOMOL, including reading the protected chatflow and sending JSON prediction requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect FlowiseAI connector schemas, fetch the connected chatflow, and send JSON prediction requests after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup documents remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use a reviewed installer or verified package source, and validate checksums or signatures before installation.

Risk: FlowiseAI access is mediated through OOMOL-connected credentials.

Mitigation: Install only in environments where OOMOL-mediated access is acceptable, and confirm write action payloads before execution.

## Reference(s):

- [FlowiseAI homepage](https://flowiseai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-flowiseai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, authenticated oo CLI and a connected FlowiseAI account.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
