## Description:

This skill helps agents operate PDFMonkey through the OOMOL-connected oo CLI for reading, creating, and updating PDFMonkey data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PDFMonkey from an agent session through OOMOL's connector, including inspecting action schemas, creating documents, retrieving document details, polling document cards, listing templates, and checking the connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not run those installer commands automatically; install the oo CLI from a trusted, versioned source and verify the installer or package before execution.

Risk: Write actions can create PDFMonkey documents or queue PDF generation.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running write actions.

Risk: PDFMonkey actions are mediated through OOMOL-connected credentials.

Mitigation: Use the skill only when the user accepts OOMOL as the intermediary and has connected the appropriate PDFMonkey account.

## Reference(s):

- [PDFMonkey homepage](https://pdfmonkey.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pdfmonkey)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may produce oo CLI commands, PDFMonkey action payloads, status summaries, setup guidance, and follow-up instructions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
