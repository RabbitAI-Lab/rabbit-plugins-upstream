## Description: <br>
Helps an agent create a brand-level social media strategy that chooses focused channels, defines a business-tied objective and strategic wedge, sets a realistic cadence, and writes social-strategy.md. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, founders, and social media operators use this skill to set or reset a brand's social media strategy before content pillars and calendars are created. It helps choose 1-3 channels, name dropped channels, connect the strategy to a business objective, and define a sustainable operating model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A broad phrase such as a request for a social media strategy could activate the skill unexpectedly. <br>
Mitigation: Use explicit routing or review the selected skill before acting when the user request is ambiguous. <br>
Risk: The generated social-strategy.md may make channel, cadence, or measurement recommendations that do not fit the current brand context. <br>
Mitigation: Review the generated strategy against brand-profile.md, audience.md, content-pillars, and platform-native analytics before using it operationally. <br>
Risk: If brand, audience, or content-pillar inputs are missing or stale, the strategy can become guesswork. <br>
Mitigation: Create or refresh the foundational inputs before relying on the strategy for channel selection and operating cadence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/social-strategy) <br>
- [Channel Selection](artifact/references/channel-selection.md) <br>
- [Goals and Measurement](artifact/references/goals-and-measurement.md) <br>
- [Operating Model](artifact/references/operating-model.md) <br>
- [Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, text] <br>
**Output Format:** [Markdown file named social-strategy.md with concise strategy guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads existing brand, audience, and content-pillar documents when available; does not post to social accounts or access analytics.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.json release.version and artifact/SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
