## Description:

Analyzes outdoor sports videos to flag possible injuries and sudden health risks, then provides structured reports and timely warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Outdoor event organizers and response teams can submit sports footage to identify possible falls, visible injuries, signs of discomfort, and movement risks, and receive a structured analysis with suggested response steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Participant footage may be sent to the provider, including when users expect analysis to be disabled.

Mitigation: Confirm authorization to share the footage before running the skill; do not rely on --export-env-only to prevent uploads.

Risk: The skill may provision an account and store access tokens without clear user controls.

Mitigation: Use an approved local identity and review credential storage and account activity when installing and operating the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Report links]

**Output Format:** [Structured sports risk analysis report with findings, recommendations, and a report link when available; Markdown for report listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes detected risk indicators and suggested response steps.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
