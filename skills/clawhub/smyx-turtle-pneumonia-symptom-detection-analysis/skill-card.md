## Description:

Analyzes fixed turtle enclosure camera video or image inputs for visual signs associated with abnormal open-mouth breathing, mucus, nasal discharge, posture changes, and related pneumonia risk warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, keepers, breeders, and reptile health staff use this skill to submit turtle enclosure media for a structured visual warning report about abnormal breathing signs and to query cloud-stored historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Turtle videos or video URLs may be sent to the Life Emergence service for analysis.

Mitigation: Use only media appropriate for third-party processing and avoid sensitive footage until API destinations and deletion controls are documented.

Risk: The skill may silently create or reuse a cloud identity and query cloud-stored historical reports.

Mitigation: Run in an isolated workspace and review account-binding and retention behavior before installing in a shared or production environment.

Risk: Service tokens may be stored in a local workspace database for report and history access.

Mitigation: Protect the workspace, rotate or delete tokens when no longer needed, and avoid sharing the workspace directory.

Risk: The skill produces visual warning reports, not veterinary diagnoses or prescriptions.

Mitigation: Treat outputs as screening guidance and route severe or repeated warnings to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON reports with recommended actions and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include turtle breathing metrics, mucus or nasal discharge observations, posture signals, warning levels, disclaimers, and cloud report links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
