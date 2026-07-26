## Description: <br>
IV Rank and IV Percentile analysis showing where current implied volatility stands relative to its 252-day history, with IV history data and trading signals based on IV zone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External traders, analysts, and agent workflows use this skill to check whether a ticker's implied volatility is high or low relative to recent history and to frame buy-premium or sell-premium decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker symbols and related query parameters may be sent to AlphaGBM. <br>
Mitigation: Avoid including proprietary watchlists or sensitive strategy context in prompts unless sharing that information with AlphaGBM is acceptable. <br>
Risk: The skill can generate buy-premium or sell-premium suggestions that may be mistaken for personalized financial advice. <br>
Mitigation: Treat outputs as market-data analysis and review trading decisions independently before acting. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-iv-rank) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/clementgu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured JSON-style market analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ticker, current IV, IV rank, IV percentile, 52-week IV range, HV/IV ratio, volatility risk premium, zone, signal, IV history, and notable events.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
