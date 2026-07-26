## Description: <br>
Helps agents convert local Markdown files into DOCX, PDF, HTML, XLSX, CSV, JSON, XML, and related formats through a command-line Markdown export workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content creators, and technical writers use this skill to convert Markdown documents and tables into shareable document, web, data, presentation, and code-extraction outputs while keeping processing local. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local conversion writes may overwrite existing files or affect sensitive directories if paths are chosen carelessly. <br>
Mitigation: Provide explicit input and output paths, avoid sensitive directories, and confirm before writing to an existing path. <br>
Risk: Code-block extraction can create many files from a Markdown source. <br>
Mitigation: Confirm the destination directory and extraction scope before running bulk extraction. <br>
Risk: The workflow depends on the third-party md-exporter package and optional system dependencies. <br>
Mitigation: Install dependencies only from trusted sources and review them with the same care as any other local execution dependency. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/md-export-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local Markdown files and write converted output files to user-selected paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
