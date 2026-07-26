## Description: <br>
生成图文并茂的现场检查网页报告；当用户需要将检查过程中的图片和文字记录整理成结构化HTML报告时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and quality, safety, or operations teams use this skill to collect site inspection notes and photos, confirm a report outline, and generate a structured internal HTML inspection report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Inspection photos and notes may contain private facility, personnel, or safety information and are saved locally and embedded into the generated HTML report. <br>
Mitigation: Review or delete inspection_images, image_data.json, and generated report files after use, especially when handling sensitive inspection material. <br>
Risk: The skill is not a substitute for legal interpretation, professional certification, or emergency safety decisions. <br>
Mitigation: Use the generated report as an internal documentation aid and have qualified reviewers verify conclusions and remediation actions before relying on them. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-site-inspection-report) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-site-inspection-report) <br>
- [Report template](assets/report-template.html) <br>
- [Image processing script](scripts/process_images.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus generated HTML report, JSON image data, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated HTML report embeds compressed inspection images as base64 data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
