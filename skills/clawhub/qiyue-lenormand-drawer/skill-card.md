## Description:

Draw Lenormand cards from QiyueAstro -- single card, three-card, relationship, decision, nine-card grid, and more. Browse the full 36-card Lenormand deck with meanings in English or Chinese. No API key needed. Free AI interpretations included (2/day per IP).

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to draw Lenormand cards, browse card and spread information, and request server-generated interpretations through QiyueAstro. It is intended for entertainment and self-reflection, with card meanings displayed from the service rather than independently interpreted by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User questions may be sent to QiyueAstro when using card draws or AI readings.

Mitigation: Tell users when a request will use QiyueAstro and advise them not to include highly personal details.

Risk: Broad activation wording could invoke the skill for general love, relationship, or decision guidance that was not clearly a Lenormand request.

Mitigation: Tighten activation wording so the skill runs only when the user clearly asks for Lenormand cards or this specific QiyueAstro reading tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-lenormand-drawer)
- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro OpenClaw Lenormand API](https://qiyueastro.com/api/v1/openclaw/lenormand)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with card images, card data, meanings, and optional server-generated reading text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses English or Chinese content returned by QiyueAstro; AI interpretations are limited to the service quota when explicitly requested.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
