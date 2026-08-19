## Description:

Queries 1688 product bestseller rankings to support wholesale sourcing, supplier comparison, and product discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, sourcing researchers, and commerce operators use this skill to find hot-selling 1688 wholesale products, compare suppliers, and filter rankings by keyword, date, price, volume, seller type, logistics, and service attributes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox network calls, API keys, and local result caching.

Mitigation: Install only after review, store API keys through LinkFox's official site or trusted secret handling, and avoid sharing cached result files that may contain sourcing data.

Risk: Ranking calls consume paid LinkFox credits.

Mitigation: Confirm the user understands the 9-credit cost before high-frequency use, and ask before repeating or broadening queries.

Risk: The bundled onboarding flow can request SMS codes, create or access accounts, list paid plans, and produce payment QR codes.

Mitigation: Prefer self-service account setup outside the agent, and require explicit confirmation before sending SMS codes, logging in, selecting a plan, or displaying a payment QR code.

Risk: Feedback may be sent to a separate LinkFox feedback endpoint.

Mitigation: Avoid including sensitive user or business details in feedback content, and disclose feedback submission when it is relevant to the user's task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-dld-product-billboard)
- [DLD Product Billboard API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, tabular ranking summaries, product links, image links when available, and saved JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries consume 9 LinkFox credits per call; larger API responses are summarized while the full JSON response is saved locally.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
