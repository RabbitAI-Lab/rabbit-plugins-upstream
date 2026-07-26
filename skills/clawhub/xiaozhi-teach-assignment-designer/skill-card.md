## Description: <br>
Helps teachers design differentiated assignments, scoring rubrics, feedback templates, and follow-up data handoffs from lesson goals and student-learning evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers use this skill to turn a knowledge point, lesson emphasis, or student-learning summary into leveled homework task cards, scoring criteria, and concise feedback templates. It is intended for teacher review and classroom use, not automatic grading or independent student placement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Assignment results sent to student-analysis workflows may contain sensitive student information. <br>
Mitigation: Confirm organizational permission before sharing de-identified results, and avoid real names, home addresses, parent identities, and individual score comparisons. <br>
Risk: Leveled assignment output could be mistaken for automatic grading or final placement decisions. <br>
Mitigation: Use the skill output as teacher-reviewed assignment design and scoring guidance; the artifact states that it outputs rubrics rather than automatic grading. <br>
Risk: A/B/C differentiated task cards may be unsupported when no student-learning summary is available. <br>
Mitigation: When student context is unavailable, use the artifact's basic-assignment fallback and label the output as lacking student-learning evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer) <br>
- [Publisher profile](https://clawhub.ai/user/qizhitang) <br>
- [assignment-rubric.md](references/assignment-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text with assignment plans, leveled task cards, rubrics, and feedback templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include A/B/C differentiation, estimated completion time, scoring criteria, de-identified feedback templates, and student-analyzer handoff fields.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
