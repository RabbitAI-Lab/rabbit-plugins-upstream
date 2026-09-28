## Description:

Analyzes video of an older adult's hand at rest to report possible tremor, motion measurements, and screening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and health-support staff can use this skill to screen resting-hand videos for possible tremor and review measurement summaries or historical reports. Results are not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health-adjacent video or video URLs may be sent to external cloud services.

Mitigation: Confirm consent and cloud-processing suitability before submitting videos or URLs.

Risk: The skill may silently create or reuse a backend identity, persist account tokens locally, and retrieve reports associated with that identity.

Mitigation: Review account linkage and local token storage before installation; restrict access to stored credentials and historical reports.

Risk: Tremor screening results could be mistaken for a diagnosis.

Mitigation: Treat findings as screening prompts and seek clinical assessment for concerning results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON; historical reports may appear as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tremor frequency, amplitude, risk prompts, and report links]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
