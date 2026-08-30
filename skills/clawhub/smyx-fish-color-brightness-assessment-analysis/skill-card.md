## Description:

Assesses ornamental fish color vibrancy from aquarium images or videos by extracting HSV color signals, comparing them with species-specific baselines, and producing a structured vibrancy report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate ornamental fish color brightness from fixed aquarium camera, smart aquarium, phone image, video, or URL inputs and to retrieve historical color assessment reports. It supports husbandry review by reporting vibrancy scores, HSV measurements, baseline comparisons, trends, and non-diagnostic recommended actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images, videos, and report-history requests are sent to the publisher's cloud-backed service.

Mitigation: Use the skill only with media and report data approved for that publisher service, and review endpoint configuration before deployment.

Risk: The skill can silently create or reuse an identity and store service tokens locally.

Mitigation: Require token-storage documentation and a way to inspect or delete stored identity data before installation.

Risk: The skill accepts URL inputs for backend processing.

Mitigation: Apply URL allowlisting and permission review before enabling URL-based analysis.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured analysis reports with report links and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include HSV measurements, vibrancy score, baseline comparison, trend fields, alert level, recommended actions, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
