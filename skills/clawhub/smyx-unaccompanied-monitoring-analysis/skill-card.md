## Description:

Analyzes home-monitoring images or video for prolonged periods without interaction or visitors and provides care reports and reminders for families of older adults living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and caregivers use the skill to review home-monitoring footage for extended periods without visitors or interaction, receive care-oriented analysis, and access account-linked historical reports. Results supplement, rather than replace, in-person checks and professional care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring images or videos may be uploaded to Life Emergence cloud services.

Mitigation: Confirm the monitored person and family understand the upload before analyzing footage; share only necessary media.

Risk: Reports are linked to an account that may be created or reused without an explicit user prompt, and tokens may be stored locally.

Mitigation: Explain account linkage before use, restrict access to the workspace data directory, and obtain confirmation before looking up report history.

Risk: Monitoring results may be mistaken for a substitute for direct welfare checks.

Mitigation: Treat alerts as care reminders and confirm concerns through in-person checks or professional care.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text and Markdown report links or history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON detail level and saved result file]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
