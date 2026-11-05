## Description:

Analyzes facial blood-flow and emotional characteristics to produce indicators for stress, anxiety tendency, and depression tendency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and wellbeing teams can submit a face image or video to receive a structured report with stress, anxiety-tendency, and depression-tendency indicators, and can query prior reports. The skill describes these results as informational and not a substitute for professional psychological consultation or clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial recordings may be uploaded to a cloud service, and the retention and deletion policy and report recipient need confirmation.

Mitigation: Get consent and confirm the provider's retention and deletion policy and which account receives reports before uploading recordings.

Risk: Account onboarding, credential storage, destination restrictions, and Windows debug logging need review before sensitive use.

Mitigation: Request fixes for these controls before using the skill with sensitive recordings or credentials.

Risk: The --export-env-only option does not prevent uploads, and the cloud backend remains unverified.

Mitigation: Do not treat that option as an upload safeguard; confirm service behavior and data handling before sending sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured assessment text or JSON; Markdown tables for historical report listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stress scores, anxiety and depression tendency indicators, suggestions, and report links when provided by the service.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
