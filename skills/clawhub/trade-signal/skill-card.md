## Description: <br>
Real-time trade signals with executable Buy/Sell/Hold recommendations for stocks, including analysis of technicals, earnings, analyst ratings, price targets, entry and exit points, portfolio rebalancing, ETFs, and options strategies across US and global markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kslee9572](https://clawhub.ai/user/kslee9572) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent developers use this skill to request finance research and actionable trade-signal analysis for public securities. It is intended for stock, ETF, options, earnings, technical, analyst-rating, filing, and portfolio-rebalancing questions that require cited market context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A crafted query can cause the bundled query script to run unintended local code during URL encoding. <br>
Mitigation: Do not run the skill on untrusted or attacker-controlled query text until the encoder passes the query as data instead of interpolating it into executable code. <br>
Risk: Finance prompts may include private holdings, brokerage details, or planned trades that are sent to terminal-x.ai. <br>
Mitigation: Avoid submitting sensitive financial details unless external sharing with terminal-x.ai is acceptable, and disclose that prompts are sent to that service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kslee9572/skills/trade-signal) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/kslee9572) <br>
- [Terminal X homepage](https://terminal-x.ai) <br>
- [Terminal X API base](https://terminal-x.ai/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [JSON responses with cited analysis fields and agent-facing text or Markdown summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include query text, ticker symbols, Buy/Sell/Hold trade signals, price targets, technical indicators, related analysis, and citation metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
