## Description:

Analyzes fixed bedroom and dining-area camera footage to report long immobility and appetite-change behavior markers for elderly or solo-living people as an observation aid, not a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, community doctors, and care-platform developers use this skill to generate behavior-change reports from long-duration home camera footage covering bedroom and dining areas. It is intended to surface observation signals such as extended bed time and reduced eating behavior while avoiding medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom and dining camera footage and mental-health-related report data may be sent to external services.

Mitigation: Do not use with real people or sensitive footage unless users receive explicit consent, destination, retention, and data-use disclosures and the deployment limits stored outputs to necessary behavior metrics.

Risk: Plaintext development endpoints are present in the released artifact.

Mitigation: Remove development HTTP configuration and require production HTTPS endpoints before installation or use.

Risk: The skill creates or reuses an internal identity and persists credentials locally.

Mitigation: Require clear account-behavior disclosure, secure token storage, and token rotation or revocation controls before deployment.

Risk: Behavioral markers could be misunderstood as a depression diagnosis or medical treatment recommendation.

Mitigation: Present outputs only as observation signals, keep the non-diagnostic framing, and route strong signals to qualified caregiver or clinician review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented structured report content with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior metrics, alert messages, recommended actions, report links, and historical report tables.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
