## Description:

Predict when a person's brain works best from their sleep, using the WhenPeak performance-intelligence API, and turn it into concrete scheduling advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whenpeak](https://clawhub.ai/user/whenpeak)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn self-reported sleep, sleep quality, and optional exercise details into timing advice for meetings, exams, deep work, presentations, daily planning, and similar scheduling decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided sleep, sleep quality, and optional exercise or sleep-fragmentation details to WhenPeak.

Mitigation: Disclose the API call before sending data and skip the call if the user does not want those details shared.

Risk: Suggestions to connect Apple Health, wearable history, or screenshots would involve sharing more health-related information with WhenPeak.

Mitigation: State the added data-sharing implication when making that suggestion and let the user decide.

Risk: Scheduling advice based on a single self-reported night can be low confidence and should not be treated as medical or diagnostic guidance.

Mitigation: Frame outputs as timing guidance, surface low confidence briefly, and avoid medical, diagnostic, or guaranteed-outcome claims.

## Reference(s):

- [WhenPeak documentation](https://whenpeak.com/docs)
- [WhenPeak homepage](https://whenpeak.com)
- [WhenPeak public API host](https://api.whenpeak.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown prose with optional shell commands and an optional PNG chart file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call WhenPeak public endpoints and may write a single-day performance chart PNG when requested.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
