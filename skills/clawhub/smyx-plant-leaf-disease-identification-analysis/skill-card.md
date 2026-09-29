## Description:

Analyzes plant leaf images or videos through a cloud service and returns disease-identification reports and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, greenhouse operators, and farm inspectors use this skill to request preliminary plant leaf disease assessments and review past reports. Results are guidance rather than a confirmed diagnosis or chemical treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or supplied URLs are sent to an external cloud service.

Mitigation: Review the service's data retention and privacy practices before submitting sensitive media or URLs.

Risk: The skill creates or reuses a persistent identity and stores account tokens in a local workspace database.

Mitigation: Confirm that identity-linked storage is acceptable, restrict access to the local database, and ask the publisher about token handling and account deletion.

Risk: The implementation does not cleanly match its advertised plant-diagnosis purpose, so results may be unreliable.

Mitigation: Review the integration before installation and confirm important diagnoses with a plant-health specialist.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Text or JSON analysis report with optional Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list cloud report history or save results to a local file.]

## Skill Version(s):

1.0.12 (source: ClawHub release; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
