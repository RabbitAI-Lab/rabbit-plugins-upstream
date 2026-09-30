## Description:

Helps agents convert, merge, split, edit, and extract data from PDFs through a connected PDF.co account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers working with PDFs can use this skill to convert documents, assemble or edit PDFs, and extract text, tables, or invoice data. Optional approved functions and triggers can automate these tasks through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF documents or extracted data may be sent through Maton to PDF.co.

Mitigation: Use only approved documents; avoid regulated or highly sensitive content and share only the data needed for the task.

Risk: Writes, connections, functions, and triggers can change documents or create ongoing automation.

Mitigation: Confirm each operation separately and grant only the access needed; prefer OAuth over API keys.

Risk: Third-party destinations or event handlers can send data outside the intended workflow.

Mitigation: Do not enable external destinations or event handlers unless explicitly requested and the data flow is understood.

## Reference(s):

- [PDF.co skill release](https://clawhub.ai/byungkyu/skills/pdf-co)
- [PDF.co API reference](https://docs.pdf.co/api-reference)
- [Maton homepage](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF.co results depend on the connected account and the approved document or automation task.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
