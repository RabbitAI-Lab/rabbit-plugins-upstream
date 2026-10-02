## Description:

Analyzes images or video of a snake's open mouth for visible signs of stomatitis and provides a risk assessment and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Snake keepers, breeders, and reptile-care teams use the skill to review mouth images or videos for possible oral lesions, receive a risk-level report, and retrieve prior reports. Results support monitoring and veterinary follow-up, not a definitive diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snake images, videos, URLs, and report history are processed by a configured cloud service.

Mitigation: Install only if this data transfer is acceptable; use a dedicated workspace or account where possible.

Risk: The skill may automatically create or reuse an identity and store authentication tokens locally.

Mitigation: Avoid environments with sensitive unrelated identity files, and review or remove the workspace SQLite database after use.

Risk: Image-based assessments may be unreliable when the mouth is obscured or image quality is poor.

Mitigation: Treat results as screening guidance, not a diagnosis; seek a reptile veterinarian for concerning findings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured assessment or Markdown report; optional JSON output and Markdown report-history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed oral signs, a risk level, suggested next steps, and a report link.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
