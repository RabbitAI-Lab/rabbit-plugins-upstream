## Description: <br>
Converts PPT, PPTX, or existing PDF files into watermarked PDFs with configurable text, layout, opacity, rotation, color, and optional web-based parameter tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avocadoleaf-highfive](https://clawhub.ai/user/avocadoleaf-highfive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, and document owners use this skill to convert presentations or PDFs into watermarked PDFs for internal materials, batch watermarking, and client deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted Office files processed through LibreOffice carry ordinary document-conversion risk. <br>
Mitigation: Keep LibreOffice patched and isolate conversion when handling untrusted presentations. <br>
Risk: Broad trigger wording could lead to use as a generic converter rather than a watermarking workflow. <br>
Mitigation: Confirm the requested task is PDF watermarking before running conversion commands. <br>
Risk: Sensitive source presentations may leave temporary conversion files during local processing. <br>
Mitigation: Remove temporary conversion outputs after running the skill on sensitive material. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration; generated artifacts are PDF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local document conversion and PDF watermarking; the optional HTML UI produces JSON configuration for watermark settings.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
