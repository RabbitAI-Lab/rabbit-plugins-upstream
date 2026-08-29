## Description:

Analyzes child-bedroom night audio and video to detect bedtime crying, fear-of-dark behavior, and nightmare awakenings, then returns structured soothing actions such as soft night-light use, prerecorded parent audio, lullabies, or parent notification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and smart-home developers use this skill to analyze authorized child bedroom or nursery night media, identify unrest events, and produce structured reports and gentle soothing recommendations. It is intended for behavior detection and caregiver support, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child bedroom audio, video, or media URLs may be sent to cloud analysis services.

Mitigation: Use only with explicit caregiver authorization, approved cloud endpoints, a documented retention policy, and a clear rule that child media is not reused for advertising or model training.

Risk: The skill can silently create or reuse an identity and query cloud report history.

Mitigation: Review identity handling before installation, restrict report access to authorized caregivers, and confirm how tokens or service identifiers are stored and revoked.

Risk: Default configuration evidence includes development, private-network, or non-HTTPS service endpoints.

Mitigation: Confirm production configuration uses approved HTTPS endpoints and remove private or development endpoints before deployment.

Risk: Behavior detection could be mistaken for clinical assessment.

Mitigation: Present outputs as observational sleep-event analysis only, preserve the no-diagnosis boundary, and direct recurring severe events to pediatric sleep or child psychology professionals.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON text containing structured event analysis, soothing actions, recommendations, history-list results, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
