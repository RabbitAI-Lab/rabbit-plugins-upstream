## Description:

Talk to your Apple Health data \u2014 ask questions about your workouts, heart rate, activity rings, and fitness trends using AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nftechie](https://clawhub.ai/user/nftechie)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent call Transition's API for Apple Health-derived workout, activity, sleep, heart-rate, and performance insights, plus structured workout generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Apple Health-derived workouts, performance metrics, profile data, chat prompts, and possibly chat history to Transition's third-party service.

Mitigation: Review Transition's privacy policy and account controls before use, and only install the skill if this data sharing is acceptable.

Risk: The API key can expose personalized Apple Health and coaching data if it is leaked or retained after access is no longer needed.

Mitigation: Store TRANSITION_API_KEY securely, avoid logging it, and revoke the key when access is no longer needed.

## Reference(s):

- [Apple Health Skill on ClawHub](https://clawhub.ai/nftechie/skills/apple-health-skill)
- [Transition](https://www.transition.fun)
- [Transition API base URL](https://api.transition.fun)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTP API guidance and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TRANSITION_API_KEY for authenticated endpoints; one workout-of-the-day endpoint is documented as available without authentication.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
