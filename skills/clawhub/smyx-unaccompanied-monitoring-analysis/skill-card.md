## Description:

Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care platform operators use this skill to analyze home monitoring images or videos for prolonged absence of interaction or visitors and to retrieve historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private monitoring images or videos may be sent to the Lifeemergence backend.

Mitigation: Use only with explicit consent and approved media sources; confirm the configured backend endpoint before execution.

Risk: The skill can create or reuse an internal identity and store authentication tokens in the workspace.

Mitigation: Run in a controlled workspace, review local credential storage, and rotate or remove stored tokens when access is no longer needed.

Risk: Default or helper configuration may allow HTTP or non-production API endpoints.

Mitigation: Restrict outbound requests to approved HTTPS production hosts before deployment.

Risk: Monitoring results are care reminders and may be incorrect or incomplete.

Mitigation: Use results as prompts for human follow-up, not as a replacement for direct visits, emergency response, or professional care.

## Reference(s):

- [API 接口文档](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output current analysis results, saved result files, or historical report listings from the Lifeemergence API.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
