## Description: <br>
Detects whether market conditions match a Tepper-style panic-buy signal using VIX, FearScore, and a large-cap quality filter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to check whether a ticker meets a market-panic entry framework and to receive a structured signal level with supporting diagnostics. It is an informational market-signal aid, not personalized financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can present direct market-timing buy guidance from broad investing prompts. <br>
Mitigation: Treat outputs as informational market-signal analysis, require explicit confirmation before acting, and verify data and assumptions independently. <br>
Risk: Users may interpret panic-bottom or buy-signal language as personalized financial advice. <br>
Mitigation: Keep responses scoped to the documented signal criteria and avoid answering broad investing questions without financial-risk guardrails. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-tepper-signal) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON response with signal diagnostics and natural-language advice fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional ticker input; artifact describes pricing and a five-minute cache per ticker.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
