## Description:

Identifies fruit ripeness stages (green, turning, ripe, or over-ripe) from fruit image or video inputs using visual features such as color, size, and gloss, then returns a standardized ripeness grade.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External agricultural users and agent operators use this skill to grade fruit ripeness from tomato, pepper, and similar economic-crop media, supporting harvest-window decisions and report lookup. It returns visual-feature-based grading and harvest guidance for review alongside field judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fruit images, videos, or media URLs are sent to configured lifeemergence.com services for remote analysis.

Mitigation: Submit only media intended for remote processing, avoid unrelated sensitive content in the frame, and review organizational approval for the configured service before installation.

Risk: Requests can be linked to a workspace identity and local token or account state may persist across runs.

Mitigation: Use an isolated workspace for evaluation and clear the workspace data file or local SQLite/token storage when persistent account linkage is not desired.

Risk: Historical report lookup retrieves cloud-stored reports associated with the active workspace identity.

Mitigation: Confirm the intended workspace identity before listing reports and avoid sharing report links outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured analysis content, ripeness grades, report links, and optional JSON-style report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze local image/video files or media URLs, save output to a file, and list cloud-stored historical reports for the workspace-linked identity.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
