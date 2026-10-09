## Description:

Analyzes videos for possible mental-health concerns and returns structured reports, suggestions, and links to past reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use the skill to request video-based mental-health assessments, receive structured findings and suggestions, and retrieve prior reports. Results are informational and do not replace professional diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive video or URL content is sent to a remote analysis service.

Mitigation: Obtain informed consent before submitting media or URLs and review the service's data-handling practices.

Risk: Persistent local and cloud identities and locally stored authentication tokens can associate reports with earlier activity.

Mitigation: Review the skill before installation, especially in shared workspaces, and protect local credentials and report access.

Risk: Historical reports could be exposed across users without reliable identity separation.

Mitigation: Do not use report-history retrieval unless per-user identity isolation is guaranteed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include findings, suggestions, and report links; results are not a clinical diagnosis.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
