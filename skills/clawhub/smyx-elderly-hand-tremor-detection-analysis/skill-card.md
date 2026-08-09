## Description:

Analyzes fixed-camera video of an older adult's hand at rest to estimate tremor frequency, amplitude, affected side, and risk level as a screening aid rather than a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, elder-care operators, community health staff, and agent developers use this skill to analyze resting-hand video or retrieve prior reports for tremor-screening workflows. It returns objective motion-analysis indicators and risk prompts that should be reviewed by appropriate medical professionals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health-related videos and report metadata may be sent to the vendor's cloud service and associated with persistent identity records.

Mitigation: Use only with informed consent, confirm retention and deletion expectations, and avoid submitting sensitive or internal video URLs unless the service is approved for that data.

Risk: Tremor metrics and risk prompts may be mistaken for a medical diagnosis.

Mitigation: Present results as screening indicators only and route concerning findings to qualified medical review.

Risk: Cloud API behavior and historical-report access depend on configured service endpoints and credentials.

Mitigation: Review endpoint configuration, authorization, and data-handling terms before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON structured analysis report with tremor metrics, risk level, prompts, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted historical reports and may write a requested local output file.]

## Skill Version(s):

1.0.7 (source: release metadata; SKILL.md frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
