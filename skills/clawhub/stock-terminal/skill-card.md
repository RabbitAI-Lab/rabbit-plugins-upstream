## Description:

Stock terminal for AI agents that turns typed commands and natural-language market questions into read-only synthesized financial reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to provide a read-only, agent-first financial terminal for stock research, daily market briefs, ticker views, smart-money screens, and data-grounded educational market synthesis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional npm CLI path can run package code with local process permissions and access to the SentiSense API key.

Mitigation: Prefer direct REST integration through reviewed host handlers; only allow the optional npx CLI path after reviewing and approving the npm package and dependencies.

Risk: API-key handling could expose credentials if keys are placed in model-visible prompts, tool arguments, or logs.

Mitigation: Keep SENTISENSE_API_KEY in host process state and inject it only inside private request handlers, never in model context.

Risk: Generic finance or news questions could invoke the skill unexpectedly.

Mitigation: Use explicit finance and ticker routing so the skill activates only for intended stock-terminal workflows.

## Reference(s):

- [Stock Terminal on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and structured terminal-style report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only financial synthesis and implementation guidance; requires SENTISENSE_API_KEY for live API-backed data.]

## Skill Version(s):

1.9.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
