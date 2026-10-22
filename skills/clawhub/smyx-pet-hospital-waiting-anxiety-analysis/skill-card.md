## Description:

Analyzes pet waiting-area videos for visible stress signals and returns a 1–5 anxiety level to support veterinary triage and comfort decisions, not diagnosis or treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary clinic staff and pet-care teams use this skill to assess stress cues in waiting-area videos, prioritize attention to highly stressed pets, and review earlier reports. Results support observation rather than veterinary diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-hospital videos and supplied video URLs are sent to the vendor's cloud service.

Mitigation: Use only media you are authorized to share; avoid footage of uninvolved people without consent.

Risk: Cloud-linked identity and cached tokens persist for access to earlier reports.

Mitigation: Review local workspace storage and report-access practices before using history features.

Risk: Visible stress cues may vary by animal and breed, limiting the reliability of a single anxiety score.

Mitigation: Check the result against direct clinical observation; do not treat it as a diagnosis.

## Reference(s):

- [Pet health analysis API documentation](artifact/references/api_doc.md)
- [Analysis API errors and upload requirements](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON or Markdown report and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an anxiety level from 1 to 5; historical reports can be listed. Not a diagnosis or treatment plan.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
