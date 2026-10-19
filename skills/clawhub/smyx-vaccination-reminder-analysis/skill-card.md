## Description:

Matches a pet's face from an image or video to vaccination records and reports whether the recorded vaccination is due or overdue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet hospital staff, boarding providers, and insurers can check a pet's recorded vaccination status using an image or video and retrieve previous reminder reports. The result is a record-based reminder, not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, URLs, and vaccination-report queries are sent to external cloud services.

Mitigation: Confirm consent, service ownership, and data retention before submitting pet data.

Risk: The skill can silently create or reuse an internal identity and store tokens in the workspace.

Mitigation: Use an isolated workspace and confirm account creation, token handling, and cleanup expectations before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Vaccination reminder API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured vaccination reminder or historical report list, with optional JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file; does not provide medical advice.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md declares 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
