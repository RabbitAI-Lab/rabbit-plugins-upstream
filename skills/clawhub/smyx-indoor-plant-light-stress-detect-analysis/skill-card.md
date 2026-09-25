## Description:

Detects indoor plant light stress from images or videos and optional lux data, classifying insufficient, excessive, or normal light and returning care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, smart-planter operators, home gardeners, and office plant caretakers use this skill to analyze plant images or videos for light-stress symptoms and receive adjustment guidance. It can also query prior cloud-generated analysis reports associated with the current user context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags privacy and transport-security risk around cloud analysis endpoints and submitted plant images, private URLs, or account identifiers.

Mitigation: Review and configure service endpoints before installation; submit sensitive images, private URLs, or account identifiers only when the endpoints are trusted HTTPS services.

Risk: The security evidence flags persistence risk around local token and report-history storage.

Mitigation: Review the skill's local identity and report-history storage behavior before deployment, and use only in environments where that persistence is acceptable.

Risk: The security evidence flags payment-redirection and billing-flow risk.

Mitigation: Review the service endpoints and billing flow before installation or use.

Risk: The security evidence notes a dependency typo that can affect installation reliability.

Mitigation: Fix the dependency typo before relying on the skill in a production environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL input, report-list output, and optional result file writing.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
