## Description:

Analyzes pet defecation-zone video or image inputs to detect poop-cleaning events and return a robot-vacuum cleaning trigger signal with a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, smart-home developers, and agent operators use this skill to analyze dog-toilet or fixed pet defecation-zone media, identify a defecation event, and produce a cleaning trigger/report that can be connected to a robot-vacuum workflow. It is not intended for medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area images, videos, or media URLs may be sent to configured Lifeemergence cloud services.

Mitigation: Use only media you are comfortable sharing with that service, prefer a test account, and review the service's retention and access controls before using private household footage.

Risk: The skill can automatically access per-user report history.

Mitigation: Review account linkage and history-query behavior before installation, and avoid using shared or sensitive accounts unless that access pattern is acceptable.

Risk: The skill can create a local SQLite user/token store in the workspace data directory.

Mitigation: Protect the workspace data directory, avoid committing local token stores, and rotate or remove stored credentials when testing is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API interface notes](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text reports, with optional JSON-detail output and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return cleaning trigger flags and report links; actual robot-vacuum control requires a user-side smart-home gateway or robot-vacuum API integration.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
