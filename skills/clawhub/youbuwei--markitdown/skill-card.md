## Description: <br>
Use when converting files (PDF, Word, Excel, PowerPoint, images, audio, HTML, EPUB, ZIP, YouTube URLs) to Markdown for LLM pipelines, indexing, and analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youbuwei](https://clawhub.ai/user/youbuwei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert documents, media, web content, and archives into Markdown for LLM pipelines, indexing, and analysis. It is useful when extracting structured text from PDFs, Office files, images, audio, HTML, EPUB, ZIP files, or YouTube URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document parsing and URL conversion can expose the agent environment to normal file, parser, and network-access risks. <br>
Mitigation: Use the skill only on files and URLs selected by the operator, avoid untrusted inputs, and review network-dependent conversions before running them. <br>
Risk: Installing optional MarkItDown plugins or system tools changes the execution environment and may add third-party code paths. <br>
Mitigation: Install only the package extras, plugins, and tools needed for the intended formats, and accept them only after reviewing their source and trust posture. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/youbuwei/markitdown) <br>
- [MarkItDown upstream project](https://github.com/microsoft/markitdown) <br>
- [ClawHub skill page](https://clawhub.ai/youbuwei/markitdown) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce large Markdown output when converting large documents, archives, or embedded data.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
