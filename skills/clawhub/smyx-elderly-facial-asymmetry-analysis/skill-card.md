## Description:

Analyzes frontal elderly face images or short videos to estimate facial asymmetry, mouth-corner deviation, related geometric indicators, risk level, and report links for auxiliary screening workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, health-monitoring operators, and developers use this skill to submit elderly facial images or videos for structured facial-asymmetry screening reports and historical report lookup. The output is a screening aid only and is not a medical diagnosis or emergency decision tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly facial images, videos, and report queries are sent to configured Life Emergence cloud APIs.

Mitigation: Use only with informed consent from the person recorded or their guardian, and avoid submitting unnecessary or highly sensitive media.

Risk: The skill may silently create or reuse an identity and store tokens in the workspace data directory.

Mitigation: Review local workspace data storage, protect the data directory, and rotate or remove stored credentials when access is no longer needed.

Risk: Facial asymmetry output could be mistaken for a clinical diagnosis or emergency triage decision.

Mitigation: Treat results as auxiliary screening information and seek professional medical care for suspected stroke, facial paralysis, or other urgent symptoms.

Risk: Historical report lookup retrieves cloud-hosted records with limited user control.

Mitigation: Confirm the active user identity before querying history and avoid displaying report links where unauthorized viewers can access them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an asymmetry index, mouth-corner drop side, key metrics, risk level, medical follow-up hint, historical report records, and export links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
