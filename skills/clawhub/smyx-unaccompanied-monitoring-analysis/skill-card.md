## Description:

Determines whether an elderly person living alone has gone without interaction or visitors for an extended period and produces care reminders for remote-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, family-support workflows, and agents that process home monitoring images or videos use this skill to request unattended-monitoring analysis, review structured care-alert reports, and retrieve historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home monitoring images or videos may be sent to a configured cloud service.

Mitigation: Use only with clear consent from the monitored person and confirm the intended API endpoints before installation or execution.

Risk: The skill may automatically associate account or identity data and store reusable tokens in the workspace data area.

Mitigation: Review the data-handling behavior, restrict workspace access, and clear stored tokens when the skill is no longer needed.

Risk: Security review classified the release as suspicious because sensitive media and session data are handled with automatic cloud and local persistence behavior.

Mitigation: Install only after a manual security review confirms that the cloud service, persistence behavior, and operational consent model are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and tables, JSON detail output, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file paths, public media URLs, history-list retrieval, output detail selection, and optional result-file output.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
