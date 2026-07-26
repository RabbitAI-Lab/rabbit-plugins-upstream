## Description: <br>
Automate common Word/WPS document operations on Windows via COM, including reading text, replacing text, inserting content, formatting headings, editing headers and footers, adding page breaks, merging and splitting documents, exporting to PDF or TXT, and adding images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fadeloo](https://clawhub.ai/user/fadeloo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and document operators use this skill to run local command-line automation for Microsoft Word or WPS Writer documents on Windows. It is suited for single-document editing, extraction, conversion, and layout operations where local file access is expected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, edit, create, merge, split, and export local Word/WPS documents. <br>
Mitigation: Run it only on documents you intend to automate, use copies for important files, and review output paths before execution. <br>
Risk: Merge and split operations can touch multiple input documents or produce multiple output files. <br>
Mitigation: Confirm the input list, page ranges, and output directory before running those commands. <br>
Risk: Document automation depends on local Windows COM behavior and installed Word or WPS Writer applications. <br>
Mitigation: Test commands on non-critical files in the target Windows environment before using them in routine workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fadeloo/skills/tiangong-wps-word-automation) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; script output can be plain text, DOCX, PDF, TXT, or image-modified documents.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on Windows and requires Microsoft Word or WPS Writer plus Python with pywin32.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
