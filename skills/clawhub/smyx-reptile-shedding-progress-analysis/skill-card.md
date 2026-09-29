## Description:

Analyzes reptile images or videos to assess shedding progress, flag possible retained shed, and provide care guidance and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and developers use this skill to review enclosure images or videos, track shedding stages, receive care guidance, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hidden identity flow may create or reuse accounts and expose cloud report history without a verified user identity.

Mitigation: Review the identity flow with the publisher and require verified platform identity and authorized report access before use.

Risk: Reptile media, report history, account identifiers, and locally stored tokens may be exposed or retained by the cloud service.

Mitigation: Use only if you trust the publisher and cloud service; ask for secure token storage and clear media retention and deletion policies.

Risk: Incorrect shedding assessments or care suggestions could delay veterinary attention.

Mitigation: Treat results as guidance rather than diagnosis and consult a reptile veterinarian for persistent or severe retained shed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)
- [Shedding analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON or human-readable text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shedding stage, risk alerts, care suggestions, and links to cloud reports; not a veterinary diagnosis.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
