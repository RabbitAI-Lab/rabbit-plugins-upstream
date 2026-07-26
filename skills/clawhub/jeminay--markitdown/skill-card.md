## Description: <br>
MarkItDown is a Python utility from Microsoft for converting PDF, Word, Excel, PowerPoint, image, audio, web, and text files into Markdown for structured-text extraction and LLM analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Damirikys](https://clawhub.ai/user/Damirikys) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to convert selected local files or supported URLs into Markdown so the agent can read and analyze document structure, tables, lists, and extracted text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill downloads markitdown and extra Python dependencies from PyPI. <br>
Mitigation: Install only in environments where PyPI-based dependencies are acceptable and review dependency policies before use. <br>
Risk: Converted Markdown may expose private contents from files, folders, or URLs passed to the tool. <br>
Mitigation: Process only documents and URLs the user intentionally chooses and handle generated Markdown according to the source content's sensitivity. <br>
Risk: Some conversions, such as YouTube URL processing, may require external network access. <br>
Mitigation: Use network-backed conversions only where external fetching is permitted; otherwise limit use to local files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Damirikys/markitdown) <br>
- [MarkItDown project link declared by the skill](https://github.com/microsoft/markitdown) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Configuration] <br>
**Output Format:** [Markdown text or .md files produced by the markitdown CLI, with shell commands for conversion workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and installs markitdown[all] into a local virtual environment] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
