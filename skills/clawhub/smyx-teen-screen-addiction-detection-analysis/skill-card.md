## Description:

Analyzes camera footage of adolescents for screen-looking posture and duration, then provides non-diagnostic reminders and reports for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use this skill to analyze adolescents' camera footage for prolonged screen-looking posture, review historical reports, and provide respectful screen-break reminders. Results are behavioral observations, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera footage of minors is sent to cloud services for analysis.

Mitigation: Use only with guardian and youth consent, and only when authorized to submit the footage to the configured services; avoid sensitive settings without clear retention, deletion, and access controls.

Risk: The skill silently creates or reuses persistent local identity and token state, and cloud report history can retain sensitive records.

Mitigation: Review account ownership, access controls, and local and cloud data deletion policies before installing or using the skill.

Risk: Posture-based screen-use classifications may mislabel reading or schoolwork and imply a clinical diagnosis.

Mitigation: Review results in context, distinguish studying from screen use, and treat reminders as non-diagnostic behavioral guidance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture and duration statistics, caregiver reminders, and cloud report links.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
