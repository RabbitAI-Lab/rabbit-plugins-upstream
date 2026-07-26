## Description: <br>
Converts academic papers from arXiv HTML links or local PDFs into structured Chinese reading reports with original figures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nuaalixu](https://clawhub.ai/user/nuaalixu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and students use this skill to read academic papers and produce Chinese reports that summarize background, methods, experiments, results, contributions, limitations, and commentary with selected original figures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads paper content and figures and writes extracted text, images, and report artifacts into the workspace. <br>
Mitigation: Use trusted paper URLs or local files, run the skill in an expected workspace, and review generated artifacts before sharing them. <br>
Risk: The DOCX workflow may run shell commands and can require global npm or pip package installation. <br>
Mitigation: Prefer HTML or Markdown output when possible, or preinstall DOCX dependencies in a controlled environment before using the Word workflow. <br>
Risk: PDF mode relies on page images and manual crop coordinates, which can misread numeric details or omit captions. <br>
Mitigation: Verify key figures, tables, captions, and numeric claims against the original paper before treating the report as final. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nuaalixu/skills/paper-report) <br>
- [Skill routing and report workflow](artifact/SKILL.md) <br>
- [HTML reader workflow](artifact/reader/html.md) <br>
- [PDF reader workflow](artifact/reader/pdf.md) <br>
- [HTML writer workflow](artifact/writer/html.md) <br>
- [Markdown writer workflow](artifact/writer/markdown.md) <br>
- [DOCX writer workflow](artifact/writer/docx.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated HTML, Markdown, or DOCX report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is a self-contained HTML report; Markdown output includes a report plus image directory, and DOCX output creates a self-contained Word file.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
