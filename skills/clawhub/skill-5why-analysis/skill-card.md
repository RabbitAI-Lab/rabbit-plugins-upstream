## Description: <br>
5WHY根本原因分析专属引导师，通过追问、校验和判定流程帮助用户定位设备故障、生产异常、质量缺陷等现场问题的根源。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operations teams, quality engineers, and process owners use this skill to run structured Chinese 5WHY conversations for root-cause analysis. It guides each round of questioning, validates user answers, proposes concrete countermeasures, and records the final conclusion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer failure, defect, or root-cause analysis into a strict question-and-answer workflow that may not fit every investigation. <br>
Mitigation: Invoke it intentionally when that structured 5WHY format is desired, and have responsible process or quality owners review the final conclusion and countermeasure before acting. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-5why-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-5why-analysis) <br>
- [5WHY analysis theory reference](references/theory.md) <br>
- [Conversation tracking template](references/tracking-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown-style Chinese dialogue prompts, validation results, countermeasure summaries, and final root-cause conclusions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code or external tool calls; produces structured conversational analysis for user review.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
