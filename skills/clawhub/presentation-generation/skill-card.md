## Description:

Turns briefs, documents, and spreadsheets into reviewable, source-cited slide outlines and editable presentations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations use this skill to extract cited material from briefs or files, review a slide outline, and request an editable presentation with optional PDF and slide previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Briefs and documents are uploaded to the AI Skills service or a user-configured API endpoint.

Mitigation: Only submit materials authorized for that service, and confirm the configured endpoint before uploading.

Risk: Generated slides may contain content or presentation errors.

Mitigation: Review the cited outline and final deck, including any partial results, before sharing externally.

Risk: The workflow requires a platform API key.

Mitigation: Keep the key in the configured environment variable; do not log, display, or commit it.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key setup and pricing](https://ai-skills.open-idea.net/skill-docs/presentation-generation/API-KEY.md)
- [Presentation operations and exports](https://ai-skills.open-idea.net/skill-docs/presentation-generation/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/presentation-generation/HTTP-REQUESTS.md)
- [Privacy, review, and partial results](https://ai-skills.open-idea.net/skill-docs/presentation-generation/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Source-cited slide outline and downloadable PPTX, PDF, or per-slide PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires outline review before file generation; partial results may include a PPTX without complete previews or quality checks.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
