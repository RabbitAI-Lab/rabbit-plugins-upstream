## Description:

Analyzes in-cabin DMS camera video to flag visual signs of driver facial flushing or abnormal sweating and produce health-risk reminders, structured reports, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet operators can use this skill to process driver-facing DMS video or image inputs and receive visual abnormality alerts, structured analysis output, recommendations, and links to generated reports. It is intended as a driver-assistance health awareness workflow, not as medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver face video and health-adjacent reports may be processed by the lifeemergence.com cloud service.

Mitigation: Use only after confirming driver or employee consent, retention expectations, access controls, and local privacy requirements for vehicle or fleet deployment.

Risk: The skill may create or reuse a persistent local identity, perform remote account login or registration, and store tokens locally.

Mitigation: Review account ownership and token storage before installation, avoid shared unmanaged environments, and clear local credentials when the deployment owner changes.

Risk: Visual flushing and sweating indicators are health-adjacent and may be affected by lighting, camera channel, face occlusion, or individual differences.

Mitigation: Treat outputs as driver-assistance alerts only, combine them with operational review or appropriate medical devices when needed, and avoid presenting results as clinical diagnosis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Driver Facial Flushing / Sweat Abnormality Detection API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured report with optional saved output file and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs to analyze files or URLs and to list historical reports.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
