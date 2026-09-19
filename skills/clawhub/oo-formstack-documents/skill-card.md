## Description:

Formstack Documents helps an agent read, create, update, copy, and delete Formstack Documents templates through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Formstack Documents templates from an OOMOL-connected account, including listing templates, retrieving fields, creating or copying templates, updating template content, and deleting templates after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer snippets that could be executed without integrity checks.

Mitigation: Do not let an agent run installer snippets automatically; install the oo CLI only through a trusted, verifiable method selected by the user.

Risk: Write and destructive connector actions can modify or delete Formstack Documents templates.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or delete actions.

Risk: Connector payloads may be invalid or stale if an agent relies on remembered fields.

Mitigation: Fetch the live action schema with the oo CLI before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-formstack-documents)
- [Formstack Documents Homepage](https://forms.formstack.com/products/documents)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
