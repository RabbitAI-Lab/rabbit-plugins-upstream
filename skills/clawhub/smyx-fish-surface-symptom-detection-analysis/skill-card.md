## Description:

Analyzes clear fish images or video for visible white spots, skin or fin redness, and fin damage, and returns symptom estimates and suggested next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists and aquarium operators can analyze fish images or video for visible symptoms and review structured findings, confidence estimates, and suggested next steps. The results support observation and triage; diagnosis and treatment decisions should be confirmed by an aquatic veterinarian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the skill suspicious due to reported account and credential handling, external data transmission, and behavior beyond its stated fish-image analysis purpose.

Mitigation: Review account registration and identity/token storage, confirm media uploads and data handling are authorized, and verify export-only behavior before installing.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured symptom report with confidence estimates, suggested actions, and optional Markdown history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports visible symptoms and estimates; it does not provide a veterinary diagnosis or medication regimen.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
