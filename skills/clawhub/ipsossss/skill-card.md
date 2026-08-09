## Description:

Grounded generation and precision filling of Word documents from Excel data while preserving a supplied Word template's structure and formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[libanzheng](https://clawhub.ai/user/libanzheng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and document automation agents use this skill to fill a Word target document from an authoritative spreadsheet while using a completed Word document only as a formatting and presentation reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may inspect sensitive spreadsheet and document contents, including hidden workbook data, while grounding the output.

Mitigation: Use the skill only with files that are appropriate to share with the agent and review the final document before distribution.

Risk: The artifact references a QA instruction file that is not included, which may reduce consistency of verification steps.

Mitigation: Confirm semantic and visual checks manually, including source tracing, reference-leak review, and rendered document inspection.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/libanzheng/skills/ipsossss)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with document-editing instructions and concise handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a filled .docx as the final agent artifact when suitable source, reference, and target files are supplied.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
