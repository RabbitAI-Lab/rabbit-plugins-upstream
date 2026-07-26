## Description: <br>
AI驱动的智能错题归档与分析系统，用于在学生提交错题、描述做错过程或请求错因分析时记录错题、定位根因、触发弱项预警并生成复习材料。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and learning assistants use this skill to turn wrong answers from photos, manual input, or spoken descriptions into structured records, four-dimensional cause analysis, weak-point alerts, targeted practice, and term-level reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to retain and reuse student wrong-answer history, weak-point labels, reports, reminders, and anxiety-related learning context across related skills. <br>
Mitigation: Use it only where this learning-data retention and cross-skill sharing are acceptable, and review what context is stored or passed to related learning skills. <br>
Risk: Photo or OCR-based problem intake may be unavailable or may misread the problem, and incomplete information can make root-cause analysis unreliable. <br>
Mitigation: Fall back to manual or spoken input, confirm unclear problem text and the student's solution process before analysis, and label uncertain conclusions before assigning practice. <br>
Risk: Subject-specific math and physics handoffs may duplicate analysis or share more learning context than needed if the boundaries are not followed. <br>
Mitigation: Use the documented handoff boundaries: keep this skill to the common record and four-dimensional classification layer, and pass only the required summaries to the subject-specific skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook) <br>
- [各科常见错误类型详细分类表](references/error-analysis-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown-formatted tutoring guidance, structured wrong-answer records, JSON-style handoff payloads, and report outlines.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on retained wrong-answer history, weak-point labels, reminders, and related subject-specific skills.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
