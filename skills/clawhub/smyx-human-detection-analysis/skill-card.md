## Description:

Detects personnel in target areas from surveillance video inputs using computer vision and returns structured monitoring results for access-control scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Security, facility, and operations teams use this skill to analyze surveillance video files or URLs for people in a defined area, including presence detection, counts, appearance frequency, intrusion indicators, and report-history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance media or referenced video URLs may be sent to backend services for processing.

Mitigation: Use only media approved for cloud processing, confirm consent and retention policy requirements, and avoid sensitive inputs unless governed by policy.

Risk: The skill may create or reuse account-linked identity and persist tokens or identity state in the workspace.

Mitigation: Run in a controlled workspace, review local identity and token storage before deployment, and avoid shared environments for production use.

Risk: Historical report queries may expose cloud-stored analysis records tied to the active identity.

Mitigation: Restrict execution to authorized accounts and verify report-history access controls before enabling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with structured JSON snippets, status messages, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a caller-specified file and may return cloud report-history results.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
