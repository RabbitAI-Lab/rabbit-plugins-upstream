## Description: <br>
Query Polymarket prediction markets for market odds, prices, event probabilities, and related Polymarket data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannyshmueli](https://clawhub.ai/user/dannyshmueli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to retrieve current Polymarket market data, including top markets, search results, specific market odds, and grouped events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes unauthenticated requests to Polymarket's public API when market odds are requested. <br>
Mitigation: Use it for explicit Polymarket-related prompts and only install it where public API lookups are acceptable. <br>
Risk: Returned prices are prediction-market data and may be mistaken for financial advice or guaranteed probabilities. <br>
Mitigation: Treat outputs as market data and review them before using them in decisions or user-facing guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dannyshmueli/skills/pm-odds) <br>
- [Polymarket public API](https://gamma-api.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text, with optional raw JSON from the Polymarket API script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Market outputs may include questions, Yes/No prices as percentages, 24h volume, total volume, liquidity, status, end dates, and descriptions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
