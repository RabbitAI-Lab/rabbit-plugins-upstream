## Description:

Analyzes child night-time sleep audio or video to report rollover frequency, crying, sleep talking, sleep-quality signals, and possible restless-sleep or nightmare alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and developers can use this skill to analyze child sleep recordings or report history for rollover, crying, sleep-talk, and sleep-quality indicators. Results are intended as caregiving support and not as medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child sleep recordings can contain highly sensitive video and audio and may be sent to cloud APIs.

Mitigation: Use only with clear guardian consent, trusted endpoints, and non-sensitive test data first; review data handling, retention, and access controls before real use.

Risk: Bundled configuration can reference development, private, or non-HTTPS service addresses.

Mitigation: Confirm the skill is configured for the intended production HTTPS service before installation or execution.

Risk: The skill may silently create or reuse a local identity and store tokens in the workspace database.

Mitigation: Review local account and token storage behavior, restrict workspace access, and remove stored credentials when they are no longer needed.

Risk: Sleep-quality and nightmare alerts may be mistaken for clinical conclusions.

Mitigation: Present outputs as behavior statistics and caregiving prompts only; direct persistent concerns to pediatric or sleep-medicine professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and structured JSON-style analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep-behavior statistics, alert messages, historical report lists, and exported report links; not a medical diagnosis.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
