## Description:

Review one person's health records across time, track conflicts, grade evidence, and highlight clinical risks without diagnosing or prescribing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals or family caregivers use the skill to compare one person's health records over time, organize conflicts and evidence, and prepare a review for a qualified clinician.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms could expose sensitive health history during an unrelated request.

Mitigation: Activate only for explicit medical-record requests and confirm ambiguous intent before opening history.

Risk: Health records may be exposed through the chosen processing environment or mixed-person folders.

Mitigation: Use a separate folder for each person, decide whether hosted processing is acceptable, and retain clinician review and write-approval requirements.

## Reference(s):

- [Companion article: Health Records an Agent Can Audit](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261021-medical-record-review.md)
- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/medical-record-review)
- [Project configuration template](references/AGENTS.example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables for trends, conflicts, evidence, and clinical risks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-person review based on configured health-record files; output is a draft for clinician review.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
