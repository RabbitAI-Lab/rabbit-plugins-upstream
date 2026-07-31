## Description: <br>
Convert PPT/PPTX to PDF and add customizable watermarks with diagonal, grid, or center layouts, adjustable styling, and an optional local web UI for parameter tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avocadoleaf-highfive](https://clawhub.ai/user/avocadoleaf-highfive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and operations teams use this skill to convert presentations or existing PDFs into watermarked PDF files before sharing internal materials, client deliverables, or batch-stamped documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local document processing may expose sensitive PPT/PPTX or PDF contents on the machine used for conversion. <br>
Mitigation: Run the skill only on trusted local systems, choose input files deliberately, and clean temporary directories after processing confidential material. <br>
Risk: The optional public tunnel can expose the local tuning UI beyond localhost. <br>
Mitigation: Keep the UI on localhost for sensitive work and avoid using the tunnel unless remote access is necessary and approved. <br>
Risk: The conversion workflow depends on local Python packages and LibreOffice handling user-selected documents. <br>
Mitigation: Install dependencies from trusted sources and review document sources before running local conversion commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/avocadoleaf-highfive/skills/pdf-watermark) <br>
- [LibreOffice Download](https://www.libreoffice.org/download/) <br>
- [README.en.md](artifact/README.en.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [PDF files plus JSON configuration and Markdown/bash guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local watermarked PDFs from PPT/PPTX or PDF inputs; optional HTML UI exports JSON watermark settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
