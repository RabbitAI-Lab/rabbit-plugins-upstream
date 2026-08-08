## Description:

Supports identifying high-risk behaviors and health risks through video/images, including elderly falls, precursors to heart attacks and strokes, and abnormal behaviors, issuing timely warning alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze images, video files, network media URLs, or real-time streams for fall events, abnormal behavior, and visible health-risk signals, then receive structured risk reports, alerts, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive images, videos, health-risk inferences, and identity-linked report data may be sent to the provider's cloud service.

Mitigation: Use only media that the operator is authorized to share, confirm provider retention and deletion terms before use, and avoid regulated or highly sensitive footage unless an appropriate data-processing agreement is in place.

Risk: The skill can create or reuse a local user identity and persist authentication tokens and identity state.

Mitigation: Run in a controlled workspace, restrict access to local data and SQLite storage, and clear or rotate retained identity and token state after evaluation or when changing operators.

Risk: Alert workflows may share footage, location, risk type, or report links with configured recipients.

Mitigation: Verify alert recipients, location-sharing settings, and reporting channels before enabling alert or real-time monitoring modes.

Risk: Visual risk analysis may produce incorrect or incomplete safety and health conclusions.

Mitigation: Treat outputs as advisory, review high-risk findings with a qualified human, and do not use the skill as a substitute for professional medical diagnosis or emergency response procedures.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Risk Categories and Alert Levels](artifact/references/risk_categories.md)
- [API Interface Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON text, with optional shell commands and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a local file when requested.]

## Skill Version(s):

999.999.1002 (source: server release metadata; artifact frontmatter version 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
