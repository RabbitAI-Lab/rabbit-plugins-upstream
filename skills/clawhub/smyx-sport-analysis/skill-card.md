## Description:

Conducts video safety risk analysis for outdoor sports event participants, including marathon and long-distance running scenarios, and produces structured risk reports, warnings, and first-aid suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route uploaded or URL-based sports footage to a remote analysis service for participant injury, discomfort, posture, environmental, and history-report review. The output is intended as safety-support information and does not replace professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports footage and identity data are sent to remote APIs.

Mitigation: Use only with a trusted publisher and API operator, and confirm endpoint ownership, retention policy, and authorization before processing private event videos or participant footage.

Risk: The skill silently creates or reuses identity and links report history to that identity.

Mitigation: Confirm expected account association and history-access controls before enabling report-list workflows.

Risk: Tokens may be stored locally.

Mitigation: Limit installation to trusted environments and review local token storage and cleanup expectations before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON-formatted analysis content, shell command examples, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured risk scores, warning text, first-aid suggestions, history-report tables, and exported report URLs.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
