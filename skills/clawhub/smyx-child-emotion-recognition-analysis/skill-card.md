## Description:

Identifies negative emotions such as crying, anger, fear, and distress through surveillance footage, then returns soothing reminders, caregiver notifications, structured results, and report links for homes, kindergartens, and daycare centers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, childcare staff, and developers can use this skill to analyze authorized child surveillance images or videos for negative-emotion signals and to retrieve prior child emotion analysis reports. It is intended to support awareness and follow-up, not to replace adult supervision or emergency response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive child surveillance media through a cloud API.

Mitigation: Use only with clear guardian or institutional authorization, and confirm the receiving service, retention terms, and report access controls before installation.

Risk: The security evidence reports silent identity creation or reuse and local authentication token storage with limited user-facing disclosure.

Mitigation: Review endpoint configuration, identity behavior, token storage, and cleanup controls before broad use.

Risk: Emotion-recognition results may be incorrect or incomplete and could be mistaken for a substitute for direct care.

Mitigation: Treat outputs as supportive signals for caregiver review and maintain adult supervision and emergency-response procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API interface documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links; optional local output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths, public media URLs, report listing, detail level selection, and optional output path.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
