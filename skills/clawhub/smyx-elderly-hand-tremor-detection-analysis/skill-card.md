## Description:

Analyzes video of an older adult’s resting hand for periodic shaking and reports estimated tremor frequency, amplitude, and a screening indication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and care teams can use the skill to review motion measures and a preliminary screening indication from a video of a resting hand. It supports follow-up and does not provide a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health videos may still be uploaded when the export-only option is selected.

Mitigation: Avoid real health recordings until this behavior is resolved. Before any cloud upload, confirm retention, deletion, and pricing terms and obtain informed permission.

Risk: Automatic account and credential handling is incompletely disclosed; endpoint selection, secret handling, and protection of the shared credential database need clarification.

Mitigation: Ask the publisher to resolve these handling issues before use, and protect the shared credential database.

Risk: Remote processing, account isolation, and clinical accuracy have not been verified.

Mitigation: Treat results as screening information only and seek assessment from a qualified clinician; confirm privacy and account-isolation protections before using sensitive recordings.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis result or Markdown report summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tremor frequency, pixel amplitude, affected side, screening risk level, and a medical follow-up hint; it is not a diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
