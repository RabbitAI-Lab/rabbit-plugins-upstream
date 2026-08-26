## Description:

Analyzes fixed-camera video and optional microphone input from dementia care settings to identify confusion or disorientation behaviors and produce structured orientation-soothing reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, facility operators, and home-care developers use this skill to analyze dementia-care audio/video inputs for disorientation indicators, review structured event reports, and guide staged orientation-soothing responses. It is intended to support observation and escalation workflows, not to provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive resident audio, video, and care-event data may be uploaded to cloud endpoints.

Mitigation: Use only with resident or legal-representative consent, approved cloud-processing terms, access controls, and retention and deletion rules.

Risk: Silent identity creation and persisted tokens can make report ownership and access harder to audit.

Mitigation: Review identity provisioning, token storage, token rotation, and deletion behavior before deployment.

Risk: Automatic caregiver, nurse, or soothing actions may affect real-world care workflows.

Mitigation: Require approved escalation policies, audit logs, and human oversight for care-setting use.

Risk: Behavior recognition results could be mistaken for clinical diagnosis.

Mitigation: Use outputs as behavior observations only, and route medical concerns to qualified care or medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and historical report lists when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter and release changelog mention 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
