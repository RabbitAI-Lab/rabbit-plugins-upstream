## Description:

Analyzes aquarium fish images or videos for visible white spots, hyperemia, and fin damage, then produces symptom reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and fish-care teams use this skill to review fish imagery for possible surface symptoms, receive severity alerts, and consult historical reports. Visual assessments are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish media or media URLs and account-linked identifiers are sent to a configured cloud service.

Mitigation: Use only media approved for cloud processing; avoid sensitive images or workspaces until the publisher clarifies retention, account linkage, and endpoint scope.

Risk: A silent account may be created or reused, and tokens are stored in a shared workspace SQLite database.

Mitigation: Review the account behavior before installation and restrict access to the workspace and its token database.

Risk: Visual symptom classifications can be mistaken for definitive fish-disease diagnoses.

Mitigation: Treat alerts as screening guidance and seek an aquatic veterinarian for diagnosis and treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)
- [Fish surface symptom API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured symptom report or Markdown history table; JSON detail option]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include symptom type, confidence, location, severity, alert level, recommended actions, and an optional saved file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
