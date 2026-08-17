## Description:

Analyzes child overnight audio or video to produce sleep-behavior statistics, sleep-quality signals, and possible nightmare or restless-sleep alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers integrating the skill use it to submit child nighttime sleep media or media URLs, receive structured behavior analysis and report links, and query historical sleep reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's overnight audio/video or media URLs are sent to a configured cloud service.

Mitigation: Use only with guardian consent, and confirm the endpoint, retention, deletion, and access-control policies before sending media.

Risk: The skill can silently create or reuse identity records and associate cloud reports with that identity.

Mitigation: Run it only in a workspace where the managed identity is expected, and avoid shared workspaces for sensitive child sleep reports.

Risk: Tokens or profile data may be stored locally in the workspace.

Mitigation: Restrict workspace access, rotate or remove credentials after use, and avoid committing generated local state.

Risk: Historical report queries retrieve cloud report data without a fresh confirmation step.

Mitigation: Require explicit operator confirmation before history queries in deployments handling child sleep reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the rendered report to a user-specified output file.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
