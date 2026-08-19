## Description:

Convert Markdown text to DOCX, PPTX, XLSX, PDF, PNG, SVG, HTML, IPYNB, MD, CSV, JSON, JSONL, XML files, and extract code blocks in Markdown to Python, Bash, JS, and other code files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowenliang123](https://clawhub.ai/user/bowenliang123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn Markdown source files into document, spreadsheet, image, notebook, web, data, and code-file outputs through the markdown-exporter CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates output files at paths supplied by the user or agent.

Mitigation: Use a dedicated output folder, avoid sensitive destinations, and check for existing files before export.

Risk: The code-block extraction command can write executable code files such as Python, Bash, or JavaScript.

Mitigation: Treat extracted code as untrusted until reviewed before execution or reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowenliang123/skills/markdown-exporter)
- [Project homepage](https://github.com/bowenliang123/markdown-exporter)
- [md-exporter Python package](https://pypi.org/project/md-exporter/)
- [Pandoc slide show syntax](https://pandoc.org/MANUAL.html#slide-shows)
- [Markdown Guide: tables](https://www.markdownguide.org/extended-syntax/#tables)
- [Markdown Guide: fenced code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell command examples; generated artifacts include DOCX, PPTX, XLSX, PDF, PNG, SVG, HTML, IPYNB, Markdown, CSV, JSON, JSONL, XML, LaTeX, Jira wiki markup, and extracted code files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates files at user- or agent-supplied output paths; some commands can create multiple numbered files or compressed code-block exports.]

## Skill Version(s):

4.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
