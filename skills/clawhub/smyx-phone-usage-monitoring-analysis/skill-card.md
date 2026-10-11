## Description:

Analyzes workplace videos and images for employee phone use and provides usage summaries, recommendations, and access to historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized workplace managers use the skill to review phone-use patterns in office video or images, generate monitoring reports, and retrieve past reports. Employees' privacy and applicable workplace monitoring rules must be respected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace video and images can expose sensitive employee information when sent to the cloud service.

Mitigation: Use only with authorization to monitor employees and transmit media; review notice, consent, retention, and applicable compliance requirements before use.

Risk: Automatic identity creation or reuse and locally stored tokens may give access to monitoring history.

Mitigation: Review identity creation and login, secure the local token database, and restrict access to historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Monitoring API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, JSON]

**Output Format:** [Text or JSON; historical reports can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes monitoring summaries, recommendations, report links, and optional saved results.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
