## Description:

Helps independent teachers plan diagnostic trial lessons, document observations, and create minimal student profiles with guardian consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this Chinese-language K12 workflow to interview families, assess a learner during a trial lesson, draft teacher-reviewed feedback, and establish a pseudonymized student profile and learning baseline. It covers trial-to-enrollment follow-up, not scheduling, lesson logs, or renewals.

### Deployment Geography for Use:

Mainland China (Chinese-language K12 defaults; localize consent and crisis resources for other regions)

## Known Risks and Mitigations:

Risk: Student profiles and diagnostic notes contain sensitive information about minors even when pseudonymized.

Mitigation: Confirm guardian consent before storing a profile, retain only necessary learning information, and keep real names and contact details out of the workspace.

Risk: Trial records or consent status may persist longer than intended or be shared without permission.

Mitigation: Honor sharing controls, set the stated retention window, and have the teacher review and confirm deletion of expired records.

Risk: Chinese-language K12 assumptions and mainland China crisis contacts may be inappropriate elsewhere.

Mitigation: Localize templates, consent practices, and crisis-referral channels before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic information form](artifact/references/student-basic-info-form.md)
- [5W needs interview checklist](artifact/references/needs-interview-5w-checklist.md)
- [Diagnosis card template](artifact/references/diagnosis-card-template.md)
- [Trial lesson structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Trial observation record](artifact/references/trial-observation-record.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)
- [Trial conversion follow-up scripts](artifact/references/followup-scripts-trial-conversion.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Teacher-reviewed drafts, structured student-profile records, and trial-lesson guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profiles use pseudonyms and require guardian consent; no contact details are collected or stored.]

## Skill Version(s):

2.9.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
