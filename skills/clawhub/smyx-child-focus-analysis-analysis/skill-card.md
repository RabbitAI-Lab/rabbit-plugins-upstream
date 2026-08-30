## Description:

Analyzes child study-area video from a smart desk lamp or tabletop camera to estimate visual focus indicators, per-minute focus scores, distraction periods, and historical focus reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents, teachers, and developers use this skill to analyze uploaded or URL-based child study-area video for focus scoring, distraction event statistics, and report links. It is intended as a learning-behavior support tool and not as a replacement for guardian or teacher judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child study videos and behavior reports may be sent to a configured cloud service.

Mitigation: Use only with clear guardian consent, verify the API endpoints before use, and avoid processing videos if cloud handling is not acceptable.

Risk: Persistent identity records, local workspace data, SQLite data, or reusable tokens may remain on the machine.

Mitigation: Run on trusted machines, avoid shared workspaces, and protect or clear local state between users.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text or JSON, with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focus scores, per-minute score series, distraction event types and timing, total distraction duration, focus grade, alerts, and cloud report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
