## Description:

MarkItDown is a Python utility from Microsoft for converting various files (PDF, Word, Excel, PPTX, Images, Audio) to Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeminay](https://clawhub.ai/user/jeminay)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to convert PDFs, Office documents, images, audio, video, web files, archives, and structured text formats into Markdown for downstream reading and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill downloads Python packages and transitive dependencies from PyPI.

Mitigation: Review the installation command and dependency policy before installation in controlled environments.

Risk: The skill processes local files and may fetch remote URL content for formats such as YouTube URLs.

Mitigation: Use it only on files intended for conversion, and avoid remote URL conversion when network fetching is not acceptable.

## Reference(s):

- [ClawHub MarkItDown Skill](https://clawhub.ai/jeminay/skills/markitdown)
- [Microsoft MarkItDown Repository](https://github.com/microsoft/markitdown)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text or Markdown files with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converted output depends on the input file format and installed optional dependencies.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
