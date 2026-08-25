## Description:

Analyzes child or student study videos to identify learning behavior patterns and produce structured reports with family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, caregivers, and education support staff use this skill to analyze study-session video files or URLs, review structured behavior reports, and retrieve historical learning behavior reports. The results are intended for family education support and study habit improvement, not diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child or student study videos, URLs, derived reports, and account-linked identifiers may be sent to the configured external service.

Mitigation: Use only with appropriate consent, submit the minimum necessary media, and review the configured service and data handling expectations before installation or use.

Risk: Local workspace data, SQLite records, and persisted tokens can remain on the machine after use.

Mitigation: Avoid shared machines for sensitive use and clear the workspace data directory, local database, and token files when they are no longer needed.

Risk: Behavior analysis reports could be mistaken for professional educational, medical, or psychological diagnosis.

Mitigation: Treat outputs as family education guidance only and involve qualified professionals for serious learning, behavioral, or health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Study analysis API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, risk notes, suggestions, report links, or historical report lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include externally hosted report export links and locally saved output files when the output option is used.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter is 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
