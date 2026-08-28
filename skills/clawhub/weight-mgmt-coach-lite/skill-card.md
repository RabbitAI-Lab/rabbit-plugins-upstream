## Description:

Guides users through weight-management, nutrition, blood-sugar-control, and health-check-report interpretation workflows, producing questionnaire-based or report-based lifestyle guidance with medical-disclaimer boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1027399464-tech](https://clawhub.ai/user/1027399464-tech)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to interpret health-check-report values or complete a 20-question health questionnaire, then receive weight-management, nutrition, activity, sleep, and chronic-disease lifestyle guidance. The skill is intended for general health education and report generation, not medical diagnosis, prescriptions, or emergency care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat health, lab-report, or chronic-disease guidance as medical diagnosis.

Mitigation: Keep outputs framed as general education, avoid diagnosis or medication instructions, and escalate disease, medication, acute symptom, or abnormal-result questions to licensed medical care.

Risk: Users may share sensitive health information while using the questionnaire or report-review flow.

Mitigation: Ask only for information needed for the assessment, avoid unnecessary identifiers, and clearly state that generated guidance is for reference rather than clinical care.

Risk: Built-in nutritionist referral language and a platform-blocking workaround may create compliance or user-trust concerns.

Mitigation: Keep referral prompts limited to generated reports and remove or clarify any instruction to work around platform blocking before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1027399464-tech/skills/weight-mgmt-coach-lite)
- [ClawHub publisher profile](https://clawhub.ai/user/1027399464-tech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and generated Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BMI estimates, calorie estimates, readiness scoring, lifestyle recommendations, and medical-escalation disclaimers.]

## Skill Version(s):

1.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
