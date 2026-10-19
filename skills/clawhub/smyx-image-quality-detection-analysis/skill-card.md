## Description:

Analyzes camera images and video for black or white screens, color casts, stripes, noise, and blurriness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Camera operators and maintenance teams use the skill to assess surveillance footage, identify image-quality problems, and review analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images, videos, and submitted URLs are sent to configured external services.

Mitigation: Use only with approved footage and trusted services; avoid private camera feeds and internal URLs unless access and data handling have been reviewed.

Risk: Account identity, report history, and locally cached tokens may link analyses to a user.

Mitigation: Review identity, authorization, retention, and token storage before installation; restrict access to local credentials and historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Image quality analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Structured analysis reports and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommendations, report links, and historical report listings.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
