## Description:

Screens newborn facial images or short videos for visual jaundice risk cues and returns a preliminary risk hint with a structured report and follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and clinical staff can use newborn facial images or short videos to receive a preliminary visual jaundice risk hint and suggested follow-up. The report is not a diagnosis; medium or high risk should be confirmed by a clinician using bilirubin measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Newborn facial images are sensitive personal data and may be uploaded for analysis.

Mitigation: Obtain guardian consent before use, and confirm the service's cloud processing and retention terms before submitting real infant media.

Risk: Visual color screening may be affected by lighting and the evidence does not establish the service's screening claims.

Mitigation: Treat results as preliminary only; use natural white light and confirm medium or high risk with a clinician and bilirubin measurement.

Risk: The security review identifies insufficient safeguards for identities and credentials.

Mitigation: Keep credentials protected, separate user identities, and restrict connections to trusted HTTPS destinations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured screening report with a risk hint, follow-up guidance, and report links; history results are JSON-formatted text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary visual screening output; not a clinical diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
