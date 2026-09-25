## Description:

Identifies fruit ripeness stages (green / turning / ripe / over-ripe) based on color, size and gloss features to output a standardized ripeness grade. | 通过颜色、大小、光泽度识别果实成熟度（青/转色/成熟/过熟），输出成熟度等级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural operators use this skill to grade ripeness for tomato, pepper, and similar economic crop fruit from images or video, then review structured results, harvest-window guidance, and report links. Developers can run the bundled command-line interface to submit local media or media URLs and query historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports silent provisioning and storage of local identity tokens.

Mitigation: Review workspace data storage before installation, restrict workspace access, and remove local identity or token records when the skill is no longer needed.

Risk: The security evidence reports development HTTP endpoint configuration for sensitive uploads.

Mitigation: Use only trusted production HTTPS endpoints before processing media or querying reports.

Risk: Uploaded media and report history are processed through a remote backend.

Mitigation: Use the skill only when the publisher and backend are trusted and uploaded images or videos are appropriate for that service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured ripeness grades, analysis details, harvest-window guidance, historical report listings, and export links from remote API responses.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
