## Description:

Analyzes turtle enclosure camera footage for open-mouth breathing and mouth or nasal discharge, then provides visual pneumonia-risk warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Turtle keepers, breeders, and reptile-care teams use camera footage to spot potentially concerning breathing or discharge and decide when to seek veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images, videos, and report history are processed by the configured cloud service.

Mitigation: Avoid sensitive footage unless the provider's retention and deletion practices are acceptable.

Risk: The skill creates and reuses a persistent local identity and authentication tokens for report history without an explicit setup prompt.

Mitigation: Review or isolate the workspace data directory before use and manage access to saved credentials.

Risk: Visual pneumonia-risk warnings may be mistaken for a veterinary diagnosis.

Mitigation: Treat reports as preliminary warnings and consult a qualified reptile veterinarian for diagnosis and care.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)
- [Skill API reference](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text with structured analysis results and risk guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert levels, suggested actions, and report access information.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
