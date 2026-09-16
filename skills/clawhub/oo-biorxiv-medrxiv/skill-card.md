## Description:

bioRxiv and medRxiv lets agents search and read bioRxiv and medRxiv data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research-support agents use this skill to retrieve bioRxiv and medRxiv preprint records, publication links, publisher articles, and content or usage statistics without constructing connector calls manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include commands that pipe remote installer scripts directly into a shell.

Mitigation: Review the setup path before installation; prefer a verified, versioned package or download and inspect the installer before execution, especially from elevated terminals.

## Reference(s):

- [bioRxiv and medRxiv homepage](https://www.biorxiv.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-biorxiv-medrxiv)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and a meta.executionId value.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
