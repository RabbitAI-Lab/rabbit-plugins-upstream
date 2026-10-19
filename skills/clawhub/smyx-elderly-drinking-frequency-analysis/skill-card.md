## Description:

Analyzes fixed-camera video of an older adult's cup area to count cup pickups and provide indicative low-drinking-frequency alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and elder-care teams use this skill to review cup-pickup frequency from home or care-facility video, identify possible low-drinking patterns, and consult prior reports. Cup pickups are an indirect signal, not a measure of fluid intake or a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home elder-care video and report queries are sent to a cloud service.

Mitigation: Obtain explicit consent from the elder or guardian and confirm the configured service and its data-handling practices before use.

Risk: The skill silently creates and persists local identity tokens, which can associate reports with the wrong person in a shared workspace.

Mitigation: Use a dedicated workspace, verify the active account identity, and review or clear stored workspace identity data when users change.

Risk: Cup pickups can misrepresent actual drinking, especially with shared cups, visitors, or incomplete camera coverage.

Mitigation: Treat alerts as prompts for caregiver follow-up, not a dehydration diagnosis; corroborate with the person's baseline and direct observation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [API interface and analysis fields](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or JSON; history lists as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cup-pickup counts, indicative risk alerts, suggested actions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
