## Description:

Automatically identifies wet clothing and abnormal excretion via visual AI, produces structured care reports, and helps caregivers respond to incontinence-related alerts for elderly, bedridden, and infant care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and operators use this skill to analyze uploaded or URL-based care images and videos for damp clothing, abnormal excretion, alert severity, and recommended follow-up actions. It can also retrieve cloud-stored historical incontinence alert reports for the associated user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive patient or infant care media and report history through external lifeemergence.com services.

Mitigation: Use only when those services are trusted for the media and report data involved, and confirm consent, authorization, retention, and deletion requirements before deployment.

Risk: The security summary says the skill may silently create or reuse identities and store service tokens locally.

Mitigation: Prefer a dedicated workspace and account, review local credential storage, and avoid mixing test, personal, and production care data.

Risk: The analysis is a care-support signal and may be affected by media quality, lighting, angle, clothing thickness, or service availability.

Mitigation: Require caregiver or clinical confirmation before using alerts to make care decisions, and keep manual inspection procedures in place.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Incontinence Alert Analysis API Documentation](references/api_doc.md)
- [Smyx Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or JSON analysis reports, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; accepts local media files or media URLs; can list historical cloud reports.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
