## Description:

Operate BoldSign through OOMOL's oo CLI for document, template, API credit, and template-based signature request workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect BoldSign documents and templates, check API credits, and send signature requests from existing templates through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute mutable remote installer scripts for the oo CLI.

Mitigation: Review the installation path before use and prefer verified official packages or installers with published checksums or signatures.

Risk: The send_document_from_template action changes BoldSign state by sending a signature request.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running the write action.

Risk: Authentication and provider connection steps affect the user's OOMOL and BoldSign accounts.

Mitigation: Run setup only after an auth or connection failure, and use the server-provided connection flow rather than handling raw BoldSign credentials in the agent.

## Reference(s):

- [ClawHub BoldSign Skill](https://clawhub.ai/oomol/skills/oo-boldsign)
- [BoldSign Homepage](https://boldsign.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI against the user's connected OOMOL and BoldSign accounts.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
