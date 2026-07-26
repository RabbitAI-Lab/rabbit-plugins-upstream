## Description: <br>
Convene the Trading Legends Council: ten trader personas vote independently on a requested symbol and timeframe, then a deterministic Chairman aggregates their ballots into a LONG, SHORT, or NO_TRADE second opinion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fxdavid-offbeatforex](https://clawhub.ai/user/fxdavid-offbeatforex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance-focused agents use Convene to fetch market data for a requested symbol and timeframe, run independent trader-persona analyses, and return an aggregated market-analysis verdict. The output is analysis support and a second opinion, not financial advice or a trading signal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TradingView setup may involve an API key that is persisted locally, and sharing it in chat could expose the credential. <br>
Mitigation: Prefer adding the key directly to a local environment file or secret store, avoid pasting it into chat, use the narrowest-scoped revocable key available, and rotate it if it was ever shared. <br>
Risk: The market-analysis verdict could be mistaken for financial advice or an actionable trading signal. <br>
Mitigation: Present the result as a second opinion only, require human review before acting on it, and stop rather than fabricate data when market data cannot be fetched. <br>


## Reference(s): <br>
- [Server-resolved source](https://github.com/FXDavid-OffbeatForex/tlc-hermes-skills/tree/main/skills/convene) <br>
- [TLC homepage](https://github.com/FXDavid-OffbeatForex/TLC) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summary with a ballot table, Chairman verdict, and setup or error guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local configuration during setup; stops with a plain error when required market data cannot be fetched.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
