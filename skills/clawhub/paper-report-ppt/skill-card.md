## Description: <br>
Turn research PDFs into editable group-meeting PPTX following the paper's structure; embed figures verbatim. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mlj-1212](https://clawhub.ai/user/mlj-1212) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Students, researchers, and academic presenters use this skill to convert research article PDFs into editable journal-club or group-meeting presentations with extracted figures and optional speaker notes/documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided PDFs are parsed into local Markdown, extracted images, PPTX, and DOCX artifacts. <br>
Mitigation: Only provide PDFs suitable for local processing, and review the generated work directory before sharing outputs. <br>
Risk: The generated presentation or speech draft may use an undesired language for non-Chinese papers. <br>
Mitigation: Explicitly set the desired output language before generation and review the final files. <br>
Risk: The skill runs local Python scripts and dependencies to process documents. <br>
Mitigation: Install and run it in a virtual environment or sandbox when possible. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/mlj-1212/paper-report-ppt) <br>
- [ClawHub skill page](https://clawhub.ai/mlj-1212/skills/paper-report-ppt) <br>
- [Formula rendering rules](references/formula-rendering.md) <br>
- [Image selection rules](references/image-selection.md) <br>
- [Outline templates](references/outline-templates.md) <br>
- [Slides JSON template](references/slides-json-template.md) <br>
- [Example slides JSON](references/example-slides.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated JSON, PPTX, DOCX, and quality-check files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local working files from user-provided PDFs, including parsed Markdown, extracted images, slides.json, editable PPTX, optional DOCX speech draft, and validation output.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
