## Description:

Monitors plant wilting from image, video, or URL inputs, identifies early signs before visible symptoms, and returns structured warnings for irrigation and disease-control decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, agronomists, and developers use this skill to submit plant images, videos, or URLs for early wilting monitoring, severity assessment, and cloud report lookup. Results support irrigation and disease-control decisions but should not replace field inspection or expert diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and report history are sent to the lifeemergence cloud service for analysis.

Mitigation: Review the destination service before installation and avoid submitting sensitive media unless cloud processing and retention behavior are acceptable.

Risk: The skill can create or reuse an internal account identity and store service tokens in a local workspace SQLite database.

Mitigation: Run it in a controlled workspace, protect or clear the workspace data directory after use, and review account and token handling before deployment.

Risk: Cloud report history can be fetched automatically when history-report triggers are used.

Mitigation: Limit access to authorized workspaces and accounts, and confirm users understand that report history is associated with the internal identity.

Risk: Wilting results are early-warning analysis outputs and may be incomplete or incorrect.

Mitigation: Use the output as decision support and confirm important irrigation or disease-control actions through field inspection or plant-health experts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [API interface documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with JSON-formatted analysis content, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calls cloud analysis and report-history APIs; may write results to a user-specified output path.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
