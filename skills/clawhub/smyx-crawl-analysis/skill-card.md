## Description:

Triggers diagnostic analysis when users provide video URLs or files for reptiles such as lizards, snakes, and spiders, calls a server-side API for health checks, and returns a Pet Safety Guardian health report covering scales, skin, body appearance, potential disease risks, and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit reptile or arachnid media for server-side health analysis, receive a structured health report, and query prior cloud-hosted analysis reports. The output is for health reference and is not a substitute for professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends reptile media or media URLs, plus an internal or user identifier, to the Life Emergence service for analysis.

Mitigation: Use the skill only with media that is approved for external processing, and confirm the publisher's permissions, retention, and deletion practices before installation.

Risk: The skill may silently create or reuse an account and store authentication tokens in the workspace data directory.

Mitigation: Run it only in workspaces where local token storage is acceptable, restrict workspace access, and ask the publisher to document token storage, rotation, and deletion.

Risk: The monitoring and history-report behavior is confusing because the documentation includes camera-monitoring examples while security evidence says this scope needs review.

Mitigation: Do not rely on camera-monitoring behavior unless the publisher documents and supports it consistently; review history-report access before use.

Risk: The generated health report may be incomplete or misleading for real animal care decisions.

Mitigation: Treat output as health reference only and consult a qualified veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [JSON or Markdown-style report text, with optional report export links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured reptile health analysis, warning signals, care suggestions, historical report records, and report image export links.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
