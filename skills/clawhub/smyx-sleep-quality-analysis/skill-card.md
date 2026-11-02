## Description:

Analyzes sleep-monitoring video to report sleep stages, body movement, awakenings, and possible sleep apnea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit a sleep-monitoring video or URL for a structured sleep analysis and query previous reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may register an account, store access tokens, and upload sleep footage even when analysis is disabled.

Mitigation: Before using private footage, confirm the selected account and the service's retention and deletion terms; avoid sharing its workspace database between users and request token protection and export-only behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured JSON analysis results and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sleep-stage, movement, awakening, and possible apnea results; historical reports can be listed.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
