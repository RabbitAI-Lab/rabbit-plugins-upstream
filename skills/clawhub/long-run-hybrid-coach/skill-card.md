## Description:

Maintains an adaptive 28-day running-and-strength plan from connected Garmin or Intervals.icu evidence, including reassessments, weekly planning, workout reviews, and previewed workout delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomchung](https://clawhub.ai/user/atomchung)

### License/Terms of Use:

MIT-0

## Use Case:

External athletes and coaches use this skill to keep a current goal-linked run-and-strength plan, review completed training against prescribed sessions, and prepare workout changes or deliveries after preview and explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses connected fitness-account authorization and may process training, weight, and workout history.

Mitigation: Install only when the user is comfortable authorizing that connection and using the connected fitness data for coaching decisions.

Risk: Plan changes or workout delivery can affect an athlete's training calendar.

Mitigation: Review the exact preview before confirming any plan change, workout delivery, or withdrawal.

Risk: Training advice can be misleading when evidence is missing, stale, or unsupported by the athlete's baselines.

Mitigation: Keep unavailable evidence explicit, avoid precise prescriptions without anchors, and require a lower-risk human decision for pain, illness, chest pain, dizziness, or unusual symptoms.

## Reference(s):

- [Pace and Stay Strong](https://paceandstaystrong.com/)
- [Long Run Hybrid Coach on ClawHub](https://clawhub.ai/atomchung/skills/long-run-hybrid-coach)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with plan, review, confirmation, and setup details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connected fitness evidence and one explicit confirmation before plan changes, workout delivery, or withdrawal.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
