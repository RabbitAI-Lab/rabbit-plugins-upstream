## Description:

Converts Markdown files into DOCX, PPTX, XLSX, PDF, HTML, IPYNB, CSV, JSON, XML, LaTeX, and extracted code-file outputs through agent-run conversion commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to have an agent convert Markdown documents, tables, slide decks, notebooks, and code blocks into common publishing and data-exchange formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to read input files, write converted outputs, and run conversion commands.

Mitigation: Use it in a constrained workspace, review requested file paths and commands, and avoid granting access outside the files needed for the conversion.

Risk: Server security evidence flags unclear callback, API, and credential behavior.

Mitigation: Do not provide API keys, credentials, callback URLs, or administrator privileges unless the publisher gives a clear service-specific explanation of the data flow and need.

Risk: Converted Markdown files may contain confidential or sensitive content.

Mitigation: Process only content approved for this publisher and verify generated outputs before sharing or publishing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/markdown-exporter)
- [Skill homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Markdown, Code, Configuration guidance]

**Output Format:** [Markdown guidance with shell command examples and generated document, data, notebook, presentation, HTML, or code files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inputs are file paths; outputs are written files or command stdout depending on the selected conversion mode.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
