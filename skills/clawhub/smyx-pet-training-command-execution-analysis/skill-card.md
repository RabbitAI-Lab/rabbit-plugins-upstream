## Description:

Analyzes pet-training videos or video URLs to assess whether a pet follows sit, down, and stay commands and provides a structured training report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, trainers, and developers use the skill to assess command response and posture timing from training videos and review prior training reports. It does not provide medical diagnosis or behavior therapy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Training footage or video URLs and report-history requests are sent to the LifeEmergence service.

Mitigation: Avoid private home footage and private URLs unless the publisher clarifies consent and data retention.

Risk: The skill may create or reuse a cloud-linked identity and store service tokens locally without an explicit user step.

Mitigation: Review account creation and token handling before installation; avoid sensitive account contexts until the publisher clarifies these practices.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis)
- [Pet training API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown tables and structured report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include response timing, posture match, training suggestions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
