## Description:

Predict when a person's brain works best from their sleep, using the WhenPeak performance-intelligence API, and turn it into concrete scheduling advice. Use this skill whenever the user asks when to schedule a meeting, interview, exam, presentation, deep-work block, or any important task; asks about their energy, focus, alertness, productivity timing, "peak hours", post-lunch dip, or chronotype; mentions how last night's sleep will affect today; or asks for a daily plan built around their performance curve, even if they never say the word "WhenPeak".

This skill is ready for commercial/non-commercial use.

## Publisher:

[whenpeak](https://clawhub.ai/user/whenpeak)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use WhenPeak to turn self-reported sleep timing and quality into concrete recommendations for scheduling meetings, deep work, exams, presentations, and other important tasks around predicted peak and dip windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep timing, sleep quality, optional exercise timing, and fragmented-sleep details are sent to WhenPeak's external API for predictions.

Mitigation: Send only user-provided fields needed for the request, omit unknown optional fields, and avoid sharing screenshots or connected health data unless the user understands WhenPeak's privacy practices.

Risk: Predictions from self-reported sleep can be low confidence and may lead to overconfident scheduling decisions.

Mitigation: Present recommendations as timing guidance, surface low-confidence or upgrade prompts briefly, and avoid framing the skill as medical or diagnostic advice.

Risk: The skill depends on network access to api.whenpeak.com for predictions.

Mitigation: If the API is unreachable, say so plainly and do not fabricate a prediction or performance curve.

Risk: Optional chart generation requires matplotlib and only supports single-day prediction responses.

Mitigation: Generate charts only when the host can run the dependency and the response contains a single-day 24-value curve; summarize multi-day projections in prose instead.

## Reference(s):

- [WhenPeak documentation](https://whenpeak.com/docs)
- [WhenPeak homepage](https://whenpeak.com)
- [ClawHub skill page](https://clawhub.ai/whenpeak/skills/whenpeak)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance, files]

**Output Format:** [Markdown scheduling guidance with optional JSON API output and optional PNG performance-curve chart]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-day predictions can include a chart file; multi-day responses summarize repeated peak, dip, and second-peak timing without charting.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
