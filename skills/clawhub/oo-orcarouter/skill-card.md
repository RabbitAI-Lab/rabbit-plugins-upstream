## Description:

OrcaRouter helps an agent operate OrcaRouter through a connected OOMOL account for reading, creating, and updating OrcaRouter resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to let an agent inspect OrcaRouter schemas, list available models, and create chat completions, embeddings, or Anthropic-format messages through their connected OOMOL/OrcaRouter account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can send user-provided content to OrcaRouter and may incur account usage or billing.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: The skill depends on a signed-in oo CLI and connected OOMOL/OrcaRouter account, so failed actions may require user account setup.

Mitigation: Run setup or connection steps only after an authentication, connection, or billing error, and direct the user to the relevant OOMOL flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-orcarouter)
- [OrcaRouter Homepage](https://www.orcarouter.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON action responses from the OOMOL oo CLI when live OrcaRouter actions are executed.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
