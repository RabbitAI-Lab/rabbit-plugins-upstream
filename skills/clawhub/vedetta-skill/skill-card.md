## Description: <br>
Vedetta provides pay-per-call crypto, US stock, and macro market intelligence over x402 micropayments (USDC on Base), including analyst reads, divergence verdicts, predictions, screeners, and track records without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lacryptorina](https://clawhub.ai/user/lacryptorina) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use Vedetta to request current, read-only market research for crypto assets, US stocks, and macro instruments. The skill helps route paid calls, run the x402 payment client, parse structured JSON responses, and preserve the descriptive research framing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill signs x402 USDC micropayments for market research calls, so wallet credentials and per-call spending need care. <br>
Mitigation: Use a dedicated low-balance wallet, keep the private key local, verify the endpoint and quoted price before paid calls, and abort if the offer exceeds the documented price. <br>
Risk: Market research responses could be mistaken for financial advice or trading instructions. <br>
Mitigation: Present outputs only as descriptive research, include the disclaimer, and avoid treating stance or confidence fields as buy, sell, or portfolio guidance. <br>
Risk: API response content may contain data that should not control local wallet actions, shell commands, or configuration changes. <br>
Mitigation: Treat responses as data for summarization and analysis only; do not execute response text or use it to trigger wallet or system changes. <br>


## Reference(s): <br>
- [Vedetta homepage](https://vedetta.dethboy.com) <br>
- [Vedetta API catalog](https://vedetta.dethboy.com/llms.txt) <br>
- [Vedetta hosted skill](https://vedetta.dethboy.com/SKILL.md) <br>
- [ClawHub skill listing](https://clawhub.ai/lacryptorina/skills/vedetta-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid x402 calls return structured JSON market research; agents must preserve the not-financial-advice framing.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter version 2.10.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
