## Description:

Identifies sleep stages, body movement, nighttime awakenings, and sleep apnea from sleep-monitoring video inputs and returns structured sleep quality reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit sleep-monitoring videos or video URLs for sleep stage, movement, awakening, and sleep apnea analysis, then view structured reports or cloud-hosted report history. The generated reports are health-related reference material and are not a substitute for professional diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep-monitoring videos, analysis reports, and report history are sensitive health-related data sent to the publisher's cloud service.

Mitigation: Use the skill only in workspaces approved for that data, avoid shared environments, and confirm retention and deletion controls before processing real user recordings.

Risk: The security evidence flags unsafe network configuration, including development HTTP endpoints and endpoint override behavior.

Mitigation: Require HTTPS production endpoints and review configuration before installation or execution.

Risk: The security evidence flags unsafe local token storage behavior.

Mitigation: Use isolated workspaces and rotate or clear credentials after testing until credential storage is fixed.

Risk: The security evidence flags dependency declaration issues.

Mitigation: Review and pin/install dependencies in a controlled environment before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration guidance]

**Output Format:** [Markdown or JSON analysis reports with report links and optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, historical report listing, and optional output-file writing.]

## Skill Version(s):

1.0.14 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
