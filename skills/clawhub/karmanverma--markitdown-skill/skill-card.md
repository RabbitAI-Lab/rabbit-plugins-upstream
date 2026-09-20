## Description:

OpenClaw agent skill for converting documents to Markdown with documentation and utilities for Microsoft's MarkItDown library across PDF, Word, PowerPoint, Excel, images, audio, HTML, and YouTube inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[karmanverma](https://clawhub.ai/user/karmanverma)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to convert files, URLs, and supported media into Markdown for documentation capture, document analysis, batch conversion, and downstream LLM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad dependency installation can add unnecessary packages to an agent environment.

Mitigation: Install in a virtual environment and prefer only the MarkItDown extras needed for the intended formats.

Risk: Optional plugins can run behavior outside the reviewed skill contents.

Mitigation: Enable plugins only when they come from trusted and reviewed sources.

Risk: External LLM, Azure, YouTube, URL, image, audio, or transcript workflows can expose sensitive inputs to third-party services.

Mitigation: Use external workflows only when policy allows the specific documents, media, URLs, and transcripts to be processed there.

Risk: Batch conversion can place generated Markdown in unintended locations or overwrite expected outputs.

Mitigation: Use explicit private output folders and check for existing Markdown files before batch conversion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/karmanverma/skills/markitdown-skill)
- [ClawHub Metadata Homepage](https://github.com/karmanverma/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown PyPI](https://pypi.org/project/markitdown/)
- [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- [Usage Guide](USAGE-GUIDE.md)
- [API Reference](reference.md)
- [Post-Install Setup](POST_INSTALL.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and Python examples; the batch utility writes Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output quality depends on the installed MarkItDown extras, optional external services, and the source document type.]

## Skill Version(s):

1.0.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
