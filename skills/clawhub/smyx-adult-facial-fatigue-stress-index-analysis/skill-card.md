## Description:

Analyzes adult face images or short videos to estimate visual fatigue and stress features, then returns a 0-100 fatigue/stress index with levels, contributing features, and directional wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, workplace wellness teams, and developers use this skill to analyze adult front-facing facial images or short videos for non-diagnostic fatigue/stress scoring and report retrieval. It is intended for personal state monitoring, smart mirrors, office health displays, and similar wellness workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images or videos, derived fatigue/stress results, report history, and identity-linked requests may be sent to the configured backend.

Mitigation: Use only after confirming user consent, backend trust, retention and deletion practices, and whether the workflow is appropriate for real personal or workplace face data.

Risk: The security review flags automatic cloud, identity, token, and local persistence behavior as requiring review before installation.

Mitigation: Verify production HTTPS endpoints, token storage behavior, and publisher documentation before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)
- [Adult Facial Fatigue / Stress API Reference](artifact/references/api_doc.md)
- [Shared Analysis API Reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue/stress score, level, feature metrics, ranked contributing features, suggestion hints, historical report records, and report export links.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
