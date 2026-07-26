## Description: <br>
Helps English teachers design CSE-first, CEFR-referenced assessments across listening, speaking, reading, and writing, with learner profiles and intervention guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
English teachers and tutoring teams use this skill to plan four-skill assessments, map learner ability against CSE with CEFR as an international reference, draft learner profiles, and prepare teaching interventions for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive student assessment profiles or CEFR/CSE levels could be written into downstream systems without clear confirmation or rollback. <br>
Mitigation: Use read-only or draft-review mode for student records, anonymize learner identifiers, and require teacher approval of the exact level, profile, and intervention fields before any write-back. <br>
Risk: Draft assessment guidance could be mistaken for final teacher scoring or ranking. <br>
Mitigation: Keep outputs as teacher-reviewed assessment frameworks and ability profiles; do not use the skill to rank students or replace teacher scoring decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment) <br>
- [CEFR can-do statements](references/cefr-can-do-statements.md) <br>
- [CEFR four-skill descriptors](references/cefr-four-skill-descriptors.md) <br>
- [Four-skill rubric](references/four-skill-rubric.md) <br>
- [Assessment template](references/assessment-template.md) <br>
- [Student ability profile template](references/student-ability-profile-template.md) <br>
- [Intervention suggestion sample](references/intervention-suggestion-sample.md) <br>
- [English growth archive sample](references/english-growth-archive-sample.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style assessment plans, learner profiles, rubrics, and intervention recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces draft CSE/CEFR mappings, four-skill profiles, and intervention fields for teacher review before use.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
