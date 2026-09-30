## Description:

Analyzes aquarium fish images or video for visible white spots, redness, and fin damage, and provides symptom reports and guidance for follow-up care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners and fish-care professionals use the skill to review camera images or video for visible fish surface symptoms, receive follow-up guidance, and retrieve past reports. Results are observational and do not replace a qualified aquatic veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish camera media, submitted URLs, metadata, and history queries are sent to configured cloud services.

Mitigation: Confirm the user accepts cloud processing and obtain explicit approval before uploading sensitive footage or looking up history.

Risk: Local identity files and stored tokens may expose or mix user data in shared workspaces.

Mitigation: Use isolated identities and token storage for each caller; avoid installation in shared workspaces without that isolation.

Risk: Visual symptom assessments can be mistaken for definitive diagnosis or treatment advice.

Mitigation: Present findings as preliminary and refer diagnosis and treatment decisions to a qualified aquatic veterinarian.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured symptom report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom confidence, affected body areas, alert level, suggested actions, and report links.]

## Skill Version(s):

1.0.12 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
