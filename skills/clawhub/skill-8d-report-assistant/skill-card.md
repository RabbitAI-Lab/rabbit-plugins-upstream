## Description: <br>
8D问题解决报告生成工具，采用分步引导+对话式信息收集模式，生成结构化详细报告，适用于汽车等行业质量问题分析场景；覆盖D1-D8八大步骤 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, manufacturing, and customer-support teams use this skill to collect 8D problem-solving details through guided dialogue and produce structured reports for quality issue analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated 8D reports may contain sensitive business details or personal contact information. <br>
Mitigation: Avoid unnecessary personal contact details, use role placeholders where possible, and review generated reports before sharing. <br>
Risk: Optional Word reports may be distributed beyond the intended quality-management audience. <br>
Mitigation: Review Word exports before external sharing and limit distribution to the intended audience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-8d-report-assistant) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-8d-report-assistant) <br>
- [8D methodology and scoring guide](artifact/references/8d-methodology.md) <br>
- [Dialogue guide and best practices](artifact/references/dialogue-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Files] <br>
**Output Format:** [Guided conversational prompts and structured Markdown reports; optional DOCX file output when Word export is requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional Word export depends on python-docx and user confirmation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter and release changelog state 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
