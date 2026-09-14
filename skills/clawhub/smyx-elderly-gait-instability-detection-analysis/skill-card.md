## Description:

Analyzes fixed-camera walking videos to estimate gait metrics such as step length, gait speed, trunk sway, and cadence, then reports gait stability indicators and a low, medium, or high fall-risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and care-technology teams can use this skill to route elderly walking videos through a gait-analysis workflow that returns objective movement metrics, fall-risk screening, recommendations, and report links. It is intended for assistive screening and monitoring rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly-person gait videos and account-linked report history may be sent to cloud services with under-disclosed persistence.

Mitigation: Use only with informed consent, confirm the destination service and retention policy, and make identity and report-history use explicit and user controlled.

Risk: Security evidence flags unsafe defaults including a development HTTP profile, silent account registration, and plaintext token storage.

Mitigation: Disable development HTTP endpoints, require HTTPS, avoid silent account registration for ordinary analysis, and avoid plaintext token storage before deployment.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes gait metrics, gait-pattern labels, fall-risk level, risk factors, recommendations, historical report listings, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
