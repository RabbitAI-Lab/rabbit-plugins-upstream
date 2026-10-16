## Description:

Analyzes pet-area images and fixed-camera videos for signs of vomiting or regurgitation, producing event observations and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, caregivers, and veterinary staff use the skill to review pet-area footage for possible vomiting or regurgitation, inspect event summaries, and retrieve past reports. Its observations do not constitute a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor images, videos, or linked media may disclose people, rooms, or routines when sent to an external service.

Mitigation: Review footage and obtain appropriate consent before use; avoid sharing media containing sensitive people or spaces unless cloud processing is acceptable.

Risk: The skill may silently create or reuse an account identity, retain authentication tokens locally, and access cloud-stored report history.

Mitigation: Use only if local account persistence and cloud report access are acceptable; restrict workspace access and review stored credentials and reports.

Risk: Visual observations may mistake similar pet behaviors for vomiting or regurgitation.

Mitigation: Treat results as observations rather than a diagnosis; confirm concerning events and seek veterinary advice when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event timing, frequency, observed material, recommendations, and report links.]

## Skill Version(s):

1.0.14 (source: published ClawHub release; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
