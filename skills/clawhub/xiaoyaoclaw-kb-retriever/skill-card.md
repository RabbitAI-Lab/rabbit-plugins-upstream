## Description:

Helps an agent search a local knowledge base and answer questions using indexed Markdown, text, PDF, and Excel files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find and cite information in a local knowledge-base directory. On request, it can also build indexes or extract PDF content for later retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent reads files in the knowledge-base directory selected by the user.

Mitigation: Choose a directory whose contents the agent may access; confirm the directory before retrieval.

Risk: Index generation and PDF extraction can create files in the knowledge base.

Mitigation: Review and confirm maintenance requests before allowing writes.

Risk: PDF and Excel handling may require optional Python packages.

Mitigation: Review and approve package installation only when the requested file processing needs it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-kb-retriever)
- [PDF reading guidance](references/pdf_reading.md)
- [Excel reading guidance](references/excel_reading.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown answers with source references and optional maintenance commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search is read-only; index generation and PDF extraction require user confirmation and write within the selected knowledge base.]

## Skill Version(s):

1.0.9 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
