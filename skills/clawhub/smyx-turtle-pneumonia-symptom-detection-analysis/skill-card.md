## Description:

Screens turtle enclosure footage for open-mouth breathing and visible nasal or oral discharge, then reports potential respiratory risk signs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Turtle keepers and veterinary staff use enclosure-camera footage to screen for visible respiratory warning signs, review risk reports, and decide when to seek veterinary assessment. Results are visual screening, not a diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure videos or video URLs are sent to a cloud analysis service.

Mitigation: Review the service's privacy and retention practices before submitting footage or URLs.

Risk: The skill creates or reuses persistent local identity and token storage linked to analysis history.

Mitigation: Review local storage and account-linking expectations before installing or accessing history.

Risk: Visual risk screening may be mistaken for a veterinary diagnosis.

Mitigation: Treat reports as warning signs only and consult a qualified reptile veterinarian for assessment.

## Reference(s):

- [Skill listing](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured risk report or Markdown history listing; JSON detail is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk indicators, suggested next steps, and report links; can save results to a file]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
