## Description:

Analyzes home-arrival camera footage and optional audio for signs of fatigue, then provides fatigue reports and suggestions for gentle smart-home care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Residents and smart-home integrators use this skill to review signs of after-work fatigue during the first 30 minutes at home and receive optional comfort suggestions, such as soothing music or rest reminders; it is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private living-room video or audio may be processed through the publisher's cloud and tied to a persistent identity.

Mitigation: Obtain explicit consent from everyone monitored, verify cloud processing and retention and deletion controls, and confirm where tokens and reports are stored before use.

Risk: Monitoring could expose household members' behavior or enable unwanted sharing of fatigue records.

Mitigation: Avoid use around visitors or in shared homes without consent, and do not share reports with employers or other third parties.

Risk: Fatigue scores could be mistaken for a medical or mental-health diagnosis.

Mitigation: Treat reports as non-diagnostic wellness suggestions and seek qualified professional advice for persistent symptoms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Fatigue care API and safeguards](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured fatigue report with care suggestions and links to historical reports; optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue scores, detected events, suggested smart-home actions, and report links.]

## Skill Version(s):

1.0.11 (source: ClawHub release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
