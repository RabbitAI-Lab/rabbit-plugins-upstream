## Description:

ByteForms lets agents inspect action schemas and retrieve ByteForms forms and form responses through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to read ByteForms data from a connected OOMOL account, including available forms, individual forms, and form responses. It guides the agent to inspect the live connector schema before making read requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup asks users to run internet installer scripts directly.

Mitigation: Review and verify the installer first, or install the oo CLI through an official signed or package-manager method.

Risk: ByteForms data is accessed through the user's connected OOMOL account.

Mitigation: Use the skill only with ByteForms data that may be exposed through that connected account.

## Reference(s):

- [ByteForms homepage](https://forms.bytesuite.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-byteforms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
