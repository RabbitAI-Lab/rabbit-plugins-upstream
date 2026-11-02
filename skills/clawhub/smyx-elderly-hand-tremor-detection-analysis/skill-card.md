## Description:

Using a fixed home camera to record video of an elderly person's hand at rest, this skill analyzes video motion for periodic shaking, extracts tremor frequency and amplitude, and identifies possible resting tremor as an early screening aid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care staff can use the skill to analyze a resting-hand video and review tremor measurements and risk-level indicators as an early screening aid. The results are not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts may mix reports belonging to different users.

Mitigation: Avoid using this version in a shared workspace until sender isolation is fixed.

Risk: The export-only option can still upload health videos, and the skill may create and save accounts or login tokens automatically.

Mitigation: Before sending footage, confirm the provider's upload, retention, and deletion terms and understand the account and token behavior.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown, Report links]

**Output Format:** [JSON or plain-text analysis report; history results can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tremor frequency (Hz), amplitude (pixels), affected side, risk level, and report links; screening information only.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
