## Description:

This skill analyzes fixed-camera videos of an elderly person's resting hand to detect periodic shaking, estimate tremor frequency and pixel displacement, and return a non-diagnostic resting-tremor risk indication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and health-monitoring operators use this skill to screen resting-hand videos for tremor indicators and review structured results or historical reports. The output is an aid for follow-up decisions, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends hand-video health data and report queries to a configured cloud service.

Mitigation: Use only with informed consent from the recorded person or responsible caregiver, and review the publisher's retention, access, and report-link handling before deployment.

Risk: The skill may create or reuse an internal identity and store user or token records locally.

Mitigation: Run it in a controlled workspace, restrict access to local data directories, and confirm account separation and token revocation procedures.

Risk: Tremor results can be mistaken for clinical diagnosis.

Mitigation: Present outputs as screening indicators only and route concerning results to qualified medical review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [API interface reference](artifact/references/api_doc.md)
- [Analysis API error reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report text with JSON-derived structured results and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tremor frequency, pixel amplitude, affected side, risk level, follow-up hint, and historical report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
