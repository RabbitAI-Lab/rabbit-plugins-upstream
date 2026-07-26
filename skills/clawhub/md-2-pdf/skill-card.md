## Description: <br>
Convert markdown files to clean, formatted PDFs using reportlab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[araa47](https://clawhub.ai/user/araa47) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agents use this skill to convert Markdown documents into styled PDF files from the command line, including documents with headings, lists, tables, links, code blocks, images, and YAML frontmatter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Markdown image links can include local image files in the generated PDF. <br>
Mitigation: Run the converter on Markdown files you trust, and review image paths before converting content from other people or automated sources. <br>
Risk: A user-specified output path can place the generated PDF somewhere unintended. <br>
Mitigation: Choose output paths deliberately and verify the destination before running the command. <br>


## Reference(s): <br>
- [md-2-pdf on ClawHub](https://clawhub.ai/araa47/skills/md-2-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated artifact is a PDF file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and Python 3.10 or newer; uses reportlab for PDF generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
