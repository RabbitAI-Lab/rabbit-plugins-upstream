## Description:

Converts common document, media, archive, web, and URL inputs into Markdown for LLM pipelines, indexing, and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youbuwei](https://clawhub.ai/user/youbuwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to install and operate MarkItDown for extracting Markdown text from PDFs, Office files, images, audio, HTML, EPUB, ZIP archives, YouTube URLs, and other inputs. It is suited to document preparation for LLM workflows, search indexing, and content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad optional installs and community plugins may introduce additional third-party code into the agent environment.

Mitigation: Install only the extras needed for the workflow, use a dedicated non-privileged virtual environment, and review community plugins before enabling them.

Risk: URL conversion, Azure document services, and LLM OCR modes may send document content to external services.

Mitigation: Avoid those modes for sensitive documents unless the destination service and data handling requirements have been approved.

Risk: Local file conversion reads files using the current process permissions.

Mitigation: Run the skill with least privilege and provide only intended input paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youbuwei/skills/markitdown)
- [Server-resolved source repository](https://github.com/youbuwei/markitdown)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell and Python code examples; converted documents are Markdown text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create Markdown output files when an output path is supplied; optional URL, OCR, plugin, audio, and cloud modes can require external packages or services.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
