## Description:

Docsend2pdf converts DocSend document URLs to PDF through OOMOL's docsend_2_pdf connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert DocSend document URLs into PDF download metadata by inspecting the live connector schema and running the convert action through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install or update the CLI only after independently trusting and verifying the installer source.

Risk: Token-bearing or private DocSend URLs may grant access to referenced content when sent to the connector.

Mitigation: Use the skill only for DocSend URLs the user is authorized to process and avoid sharing private links unnecessarily.

Risk: The skill's routing language is broader than necessary for a single conversion connector.

Mitigation: Use it only for DocSend-to-PDF conversion tasks and inspect the live action schema before running the connector.

## Reference(s):

- [Docsend2pdf homepage](https://docsend2pdf.com)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsend-2-pdf)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector returns JSON-safe PDF download metadata and execution details.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
