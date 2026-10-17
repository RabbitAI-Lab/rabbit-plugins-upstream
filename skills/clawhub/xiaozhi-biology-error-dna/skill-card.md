## Description:

Analyzes Chinese middle- and high-school biology mistakes across six dimensions to identify underlying weaknesses and suggest targeted practice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use the skill to identify patterns behind biology mistakes, plan focused practice, and request a weakness report. Long-term profiles and sharing require student consent.

### Deployment Geography for Use:

Mainland China; localize curriculum, minor-consent rules, and crisis resources before use elsewhere.

## Known Risks and Mitigations:

Risk: A minor's learning profile or parent-visible summary could be shared without appropriate consent.

Mitigation: Confirm student consent for profile use, cross-skill sharing, reminders, and any parent-visible summary before enabling each.

Risk: Curriculum assumptions or crisis referrals may be inappropriate outside mainland China.

Mitigation: Localize the curriculum, minor-consent requirements, and crisis resources before deploying in another region.

Risk: Biology questions about a student's health could be mistaken for medical advice.

Mitigation: Limit explanations to textbook biology; for personal health concerns, advise contacting a parent and a clinician rather than diagnosing or treating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [Biology error dimension table](references/biology-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language explanations and weakness reports; optional structured profile and handover data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are requested by the student; profile updates, sharing, and reminders depend on consent.]

## Skill Version(s):

2.11.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
