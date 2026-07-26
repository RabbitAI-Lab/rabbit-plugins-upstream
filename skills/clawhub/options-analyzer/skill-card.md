## Description: <br>
Options Analyzer helps agents retrieve option-chain data, calculate Greeks and implied-volatility metrics, analyze common options strategies, and recommend strategies from a market outlook and risk posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benzema216](https://clawhub.ai/user/benzema216) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to inspect public options data, compare Greeks and implied-volatility signals, estimate payoff profiles, and generate options strategy guidance for further review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public market data may be delayed, incomplete, or unavailable, which can make option-chain, IV, and Greek outputs inaccurate. <br>
Mitigation: Confirm all prices, expirations, implied volatility, and liquidity against broker or exchange data before using outputs for real-money decisions. <br>
Risk: The provided security guidance notes that IV Rank and IV Percentile use a proxy and some strategy models do not handle stock legs or different expiries correctly. <br>
Mitigation: Treat strategy analysis and recommendations as screening guidance; manually verify legs, expirations, payoff math, and risk exposure before acting. <br>
Risk: Dependency or environment drift can affect script behavior, including the Greeks calculator requirement for scipy. <br>
Mitigation: Install in a virtual environment, pin and review dependencies, and include scipy when using the Greeks calculator. <br>


## Reference(s): <br>
- [Options Analyzer ClawHub page](https://clawhub.ai/benzema216/skills/options-analyzer) <br>
- [benzema216 ClawHub profile](https://clawhub.ai/user/benzema216) <br>
- [Strategies reference](references/strategies.md) <br>
- [Greeks guide](references/greeks_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON from command-line analysis scripts, with inline shell commands and explanatory guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public market data and deterministic calculations where available; recommendations require independent review before trading.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
