## Description:

Uses product page and review evidence for a main Amazon ASIN and authorized competitors to prepare a pre-entry comparison brief with page differences, customer questions, and validation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product researchers, and developers use this skill to compare Amazon listing and review evidence before entering a market. It supports pre-entry research and validation planning, not market size, sales, profit, advertising, inventory, order, or return-rate prediction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI can run paid ARI operations and spend ARI credits after quote confirmation.

Mitigation: Run capability, profile, and quote checks before paid actions, verify the returned requestId, and proceed only after explicit user confirmation.

Risk: Direct CLI use can override the documented fixed market-entry workflow.

Mitigation: Review commands before execution and confirm that operation requests use the expected page_compare/entry workflow.

Risk: The skill requires granting an ARI API key to a third-party bundled CLI.

Mitigation: Install only when the user accepts that access, use the documented https://ari.funewa.com endpoint, and stop on endpoint or redirect blocking errors.

## Reference(s):

- [Amazon Market Entry Brief Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Market Entry Brief API Reference](artifact/references/reference.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/market-entry-brief)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional inline shell commands and ARI operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis requires a quote and explicit user confirmation before execution.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
