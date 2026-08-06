## Description:

Analyzes fixed-camera home video to detect prolonged standing, bending, and related pregnancy over-fatigue signals, producing posture metrics, rest reminders, and report links for health reference rather than medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect fixed-camera pregnancy posture analysis into smart-home, prenatal-school, community health, or pregnancy-management workflows. It is intended for visual posture statistics, fatigue-risk reminders, history lookup, and report export links, not diagnosis or medical treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pregnancy-related home camera footage and analysis history are sensitive and may be processed through the vendor's cloud service with report links.

Mitigation: Use only with explicit informed consent, limit inputs to necessary footage, protect exported reports and local workspace data, and avoid shared-device workflows unless identities are separated.

Risk: The skill may silently create or reuse a persistent local/cloud identity for analysis history.

Mitigation: Confirm the intended identity context before use, separate users on shared devices, and review local configuration or cached identity state when changing users.

Risk: The output could be mistaken for medical advice even though it is intended as health reference only.

Mitigation: Present results as posture statistics and friendly reminders, keep diagnosis and treatment decisions with qualified medical professionals, and escalate urgent symptoms to clinical care.

Risk: Visual posture detection can be unreliable when the full body is not visible, lighting is poor, camera angle is unsuitable, or clothing obscures posture.

Mitigation: Use stable full-body camera coverage with adequate lighting and treat alerts as supportive signals to review alongside user context and daily trends.

## Reference(s):

- [Pregnant posture fatigue detection API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown text containing structured analysis, JSON-style posture and fatigue-risk fields, history tables, reminder guidance, and report links; optionally saved to a local output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report export links and history-query results associated with a persistent internal identity.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
