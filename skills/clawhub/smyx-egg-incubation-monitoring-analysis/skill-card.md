## Description:

Submits turtle or snake egg images or videos for remote visual assessment and returns incubation reports or report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile breeders and keepers use the skill to submit egg images or videos for incubation-stage assessments and to retrieve earlier reports. The bundled code sends inputs to a remote service; scheduled camera capture and automatic monitoring are not implemented in the bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option may continue into analysis and upload media, while credentials can be sent to destinations not restricted by the shared network code.

Mitigation: Fix and verify export-only handling and credential destinations; use a separate workspace with dedicated service credentials.

Risk: Submitted media and URLs go to LifeEmergence services, and server retention and deletion behavior could not be verified.

Mitigation: Confirm the provider's retention and deletion controls before sending private footage.

Risk: The advertised automatic photo monitoring is not implemented in the bundle.

Mitigation: Treat this as an explicit-input submission and verify remote service behavior before relying on monitoring results.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown report or JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stage estimates, alerts, next steps, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
