## Description:

Operate Formspree through an OOMOL-connected account to list form submissions with optional filters using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Formspree submission data through an OOMOL-connected account. It is intended for Formspree read workflows where the agent should inspect the live connector schema before running an action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes one-line remote installer commands for the oo CLI.

Mitigation: Prefer a versioned, checksum- or signature-verified installation path before running installer commands.

Risk: Formspree submission data may pass through OOMOL connector infrastructure and can contain sensitive user-provided content.

Mitigation: Use the skill only when that data path is acceptable, and ask for confirmation before retrieving sensitive submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formspree)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Formspree homepage](https://formspree.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON; the skill instructs agents to inspect the live action schema before constructing payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
