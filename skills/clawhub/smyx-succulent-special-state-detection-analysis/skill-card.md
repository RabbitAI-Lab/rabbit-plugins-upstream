## Description:

Analyzes succulent images or videos for black rot, translucent leaf damage, and stretching, returning condition assessments and severity information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home growers, greenhouse operators, and florists use the skill to assess succulent images or videos for visible problems and review condition reports and past results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or submitted URLs are sent to the Life Emergence cloud service.

Mitigation: Submit only media you are comfortable sharing with that service.

Risk: The skill automatically manages a cloud identity and associates reports with it; identity and retention practices are not explicit.

Mitigation: Confirm identity and report-retention practices with the publisher before using sensitive media.

Risk: Service tokens are stored in the workspace data directory, and the Python import path is unsafe.

Mitigation: Avoid shared machines and review the installation until the publisher fixes the import path and clarifies token handling.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [Succulent analysis API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown reports or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include condition confidence, severity, and links to cloud-hosted reports; historical reports can be listed.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
