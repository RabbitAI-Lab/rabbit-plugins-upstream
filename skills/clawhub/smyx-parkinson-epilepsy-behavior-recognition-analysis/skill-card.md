## Description:

Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-monitoring developers use this skill to analyze home monitoring images or videos for tremors, convulsions, stiffness, gait abnormalities, and abnormal episode patterns. It can also return structured historical analysis reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload patient images or videos to cloud APIs, and the security evidence reports a default plaintext HTTP configuration for sensitive patient media.

Mitigation: Use only non-sensitive test media until the publisher documents HTTPS-only transport, retention behavior, and handling of uploaded medical media.

Risk: The skill may create or reuse an internal user identity, store authentication tokens in a local workspace database, and query historical reports automatically.

Mitigation: Review identity and token storage before installation, and require explicit user-controlled consent before enabling history access or uploads.

Risk: Behavior-recognition output for Parkinson's or epileptic activity can be mistaken for a medical diagnosis.

Mitigation: Treat results only as monitoring assistance and require review by an appropriate medical professional for clinical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown and JSON analysis reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
