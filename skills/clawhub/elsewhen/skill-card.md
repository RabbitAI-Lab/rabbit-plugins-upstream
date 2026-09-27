## Description:

Guides agents through a persistent Traditional Chinese historical text game using the Elsewhen service and a dedicated OpenRouter or Google AI Studio key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenplus1000](https://clawhub.ai/user/tenplus1000)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users play a persistent historical text game, choosing actions and reading the resulting story in Traditional Chinese.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A billable model API key is stored by the third-party game service.

Mitigation: Use a separate, low-credit-limit OpenRouter or Google AI Studio key and only connect if comfortable sharing it with Elsewhen.

Risk: Exposure of the Elsewhen token may allow access to saves and the stored key.

Mitigation: Keep the token private and do not share it in public logs or messages.

Risk: The game responds only in Traditional Chinese.

Mitigation: Use the skill only when the agent and user are comfortable with Traditional Chinese output.

## Reference(s):

- [Elsewhen overview](https://play.elsewhengame.com/about)
- [Elsewhen skill on ClawHub](https://clawhub.ai/tenplus1000/skills/elsewhen)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Traditional Chinese text and gameplay guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent game state is maintained by the Elsewhen service.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
