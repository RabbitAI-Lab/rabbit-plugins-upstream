## Description:

Draw Lenormand cards from QiyueAstro — single card, three-card, relationship, decision, nine-card grid, and more. Browse the full 36-card Lenormand deck with meanings in English or Chinese. No API key needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to draw or browse Lenormand cards through QiyueAstro, including single-card draws, named spreads, relationship or decision prompts, and card meanings in English or Chinese.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lenormand draw requests, including user-provided question text, may be sent to QiyueAstro's unauthenticated public API.

Mitigation: Avoid sending secrets, private identifiers, or highly sensitive personal details in the question.

Risk: The skill depends on QiyueAstro's public API availability and rate limits.

Mitigation: Handle service failures or 429 responses without aggressive retries, and direct users to QiyueAstro when the service is unavailable.

Risk: Card meanings could be misrepresented if the agent adds its own interpretation.

Mitigation: Display API-returned meanings verbatim and avoid additional synthesis or card relationship commentary.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro OpenClaw Lenormand API](https://qiyueastro.com/api/v1/openclaw/lenormand)
- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-lenormand-drawer)
- [Publisher profile](https://clawhub.ai/user/bloodymarygg)

## Skill Output:

**Output Type(s):** [Markdown, API calls, Guidance]

**Output Format:** [Markdown with direct image links and API-returned card text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include card images, card names, spread positions, keywords, meanings, and a QiyueAstro call-to-action.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
