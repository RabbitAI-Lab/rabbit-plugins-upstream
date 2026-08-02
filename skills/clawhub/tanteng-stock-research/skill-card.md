## Description: <br>
Generates concise Chinese-language stock research reports for A-share, Hong Kong, and U.S. equities using market data, recent news, regulatory checks, technical indicators, and rating criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanteng](https://clawhub.ai/user/tanteng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual investors and market researchers use this skill to produce fast stock reviews with current price context, buy/hold/sell ratings, support and resistance levels, risk notes, and action-oriented position guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces investment-style analysis that may be incorrect, incomplete, or stale if market data or news search results are missing or outdated. <br>
Mitigation: Verify market data, recent news, and cited regulatory events before using the report for investment decisions. <br>
Risk: The skill relies on market-data and web-search tools to gather stock, news, and regulatory information. <br>
Mitigation: Install only when those tools are acceptable for the deployment environment and review generated reports for source quality. <br>
Risk: The documented upgrade path includes a manual command that deletes the named old skill directory. <br>
Mitigation: Review the command and back up local skill changes before running any manual upgrade step. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tanteng/skills/tanteng-stock-research) <br>
- [Upstream Stock Research Team skill](https://clawhub.ai/skills/stock-research-team) <br>
- [Changelog](references/changelog.md) <br>
- [Market rules](references/market-rules.md) <br>
- [Rating criteria](references/rating-criteria.md) <br>
- [Technical indicators](references/technical-indicators.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown stock research report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language report with rating, operating guidance, key price levels, core thesis, and a regulatory-event risk section.] <br>

## Skill Version(s): <br>
4.0.0 (source: server release metadata and artifact changelog, released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
