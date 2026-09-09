## Description:

Through fixed enclosure cameras, the skill analyzes turtle mouth and nasal video to flag unusually frequent open-mouth breathing, mucus, or nasal discharge as visual pneumonia-risk indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Keepers, breeders, animal hospital staff, and developers can use this skill to review turtle enclosure videos or URLs for visual respiratory risk indicators and receive structured alerts, recommended non-prescriptive actions, report links, or historical report lists. It is intended to support monitoring and escalation to a professional reptile veterinarian, not to diagnose disease or prescribe treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure videos, URLs, and report queries may be sent to a remote service.

Mitigation: Use only with content that is approved for remote processing, and review the configured service endpoints before deployment.

Risk: The skill may silently create or reuse account identifiers and store tokens or user records in the workspace data directory.

Mitigation: Review local data storage behavior, isolate the workspace, and clear generated credentials or user records when they are no longer needed.

Risk: A development configuration references private HTTP endpoints.

Mitigation: Correct or document endpoint configuration before trusted use, and prefer audited production HTTPS endpoints.

Risk: The skill provides health-risk alerts that could be mistaken for diagnosis or treatment advice.

Mitigation: Keep outputs limited to visual indicators and non-prescriptive actions, and direct users to consult a professional reptile veterinarian for diagnosis or treatment.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON-style analysis fields and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include pneumonia-risk alert levels, visual symptom measurements, non-prescriptive recommended actions, disclaimers, exported report links, and historical report lists.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
