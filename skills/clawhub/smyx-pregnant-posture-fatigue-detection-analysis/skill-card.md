## Description:

Uses a fixed home camera to detect prolonged standing, bending, and related posture of a pregnant woman, track standing duration and bending frequency, assess fatigue risk, and produce rest reminders for health reference only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home users, prenatal schools, community health centers, smart-home developers, and pregnancy-app developers use this skill to analyze fixed-camera images or videos for prolonged standing, frequent bending, suspected heavy lifting, and related fatigue reminders. The outputs are health-reference posture and activity observations, not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pregnancy-related home camera footage is sensitive and may be processed through cloud services.

Mitigation: Use only with explicit informed consent from the pregnant person, confirm deletion and retention terms, restrict access, and prefer privacy-preserving body-outline modes when available.

Risk: The skill may silently create or reuse local identity state and stored tokens.

Mitigation: Review endpoint and account handling before deployment, isolate the runtime environment, and manage local state and credentials according to organizational policy.

Risk: Health-reference reminders could be mistaken for medical assessment.

Mitigation: Present results as posture and activity observations only, preserve the non-diagnostic wording, and direct users to medical professionals for symptoms or clinical concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured posture and fatigue analysis reports, reminder text, historical report tables, and optional JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture classification, standing duration, bending frequency, alert type, alert level, recommended action, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
