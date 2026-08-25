## Description:

mddoc converts Markdown files or pasted Markdown text into academically formatted Word DOCX documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trisia](https://clawhub.ai/user/trisia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, and researchers use this skill to convert Markdown papers, reports, and thesis-style content into Word documents with academic formatting for headings, body text, tables, images, and math.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup workflow may create a persistent Python environment and install unpinned packages from an external package index.

Mitigation: Review and approve the environment setup path and dependency set before running it in managed or sensitive environments.

Risk: The converter may fetch image URLs embedded in Markdown during conversion.

Mitigation: Avoid untrusted Markdown or review remote image fetching behavior before converting documents that contain external images.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [DOCX file with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs to a requested path, the input file directory, or the current directory depending on invocation.]

## Skill Version(s):

0.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
