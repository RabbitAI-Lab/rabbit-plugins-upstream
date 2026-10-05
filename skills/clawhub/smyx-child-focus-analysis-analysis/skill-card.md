## Description:

Analyzes children's study-area videos for focus scores and distraction periods, and provides reports and access to historical results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers use study-area video analysis to review a child's estimated focus scores, distraction periods, and historical reports as aids to understanding study habits, not as a substitute for direct observation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's study-area media or URLs are sent to external cloud services.

Mitigation: Obtain guardian consent before use and govern media access, transmission, and retention.

Risk: Cloud history access and silently created or reused identities may expose reports to the wrong account.

Mitigation: Confirm account ownership and restrict and audit access to historical reports.

Risk: Authentication tokens are stored locally.

Mitigation: Protect local credentials and limit access to the device and account.

Risk: Estimated focus scores can be mistaken for definitive assessments of a child.

Mitigation: Treat scores as supplementary and confirm findings through direct observation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured report or Markdown table; optional JSON output and saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated per-minute focus scores, distraction periods, and report links when available]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
