## Description:

Logo.dev enables agents to search Logo.dev brand data, retrieve structured brand metadata by domain, and build logo image URLs through the OOMOL logo_dev connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to search Logo.dev brand records, look up brand metadata, and generate logo image URLs by domain, name, ticker, ISIN, or crypto symbol.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners that execute downloaded shell or PowerShell content.

Mitigation: Prefer official, versioned installation instructions and inspect what the installer will execute before running it.

Risk: Logo.dev actions depend on the current OOMOL connector schema and the user's authenticated Logo.dev connection state.

Mitigation: Inspect the live connector schema before each action and run setup or connection steps only after a matching command failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-logo-dev)
- [Logo.dev Homepage](https://logo.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Logo.dev connector command results with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
