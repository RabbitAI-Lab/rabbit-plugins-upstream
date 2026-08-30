## Description:

BoldSign (boldsign.com). Use this skill for any BoldSign request, including reading, creating, and updating data through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected BoldSign account from an agent, including checking credits, reading document or template details, listing documents or templates, and sending signature requests from existing templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read BoldSign documents, templates, status, signer data, and account credit information from the connected account.

Mitigation: Install and use it only when the user trusts OOMOL's oo CLI and accepts that the connected BoldSign account data may be read through the connector.

Risk: The send_document_from_template action changes BoldSign state by sending a signature request from an existing template.

Mitigation: Confirm the exact payload and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-boldsign)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [BoldSign Homepage](https://boldsign.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema commands, connector run commands, JSON payload examples, and user confirmation guidance for write actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
