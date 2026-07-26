## Description: <br>
Guides an agent through voice-of-customer feedback collection, categorization, CTQ extraction, priority analysis, and report generation from user-provided customer feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external teams, and developers use this skill to analyze authentic customer or user feedback for products, services, processes, or quality workflows. It helps organize feedback, extract measurable critical-to-quality requirements, suggest improvement priorities, and produce review-ready reports after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer feedback may include confidential customer, employee, or regulated data. <br>
Mitigation: Use conversation-only output for sensitive analyses, or store generated Markdown and HTML reports only in approved locations. <br>
Risk: The analysis depends on authentic user-provided feedback and confirmed CTQ or priority decisions. <br>
Mitigation: Keep the skill's confirmation gates: do not invent feedback, and require user confirmation before final CTQ thresholds, classifications, and improvement priorities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-voc-analysis) <br>
- [Server-resolved GitHub source repository](https://github.com/duding-engicool/skill-voc-analysis) <br>
- [Server-resolved GitHub provenance commit](https://github.com/duding-engicool/skill-voc-analysis/commit/e23299fde99d615a3c8135d254714b303b8f42bf) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Conversation guidance plus Markdown and HTML report artifacts when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided feedback and user confirmation before final CTQ choices, priorities, and full report generation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
