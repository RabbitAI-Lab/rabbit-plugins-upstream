## Description: <br>
Helps an agent use trading volume and open interest as secondary confirmation for price signals, trend health, blowoffs, selling climaxes, and COT report interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bianchunhui](https://clawhub.ai/user/bianchunhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to guide an agent in volume and open-interest based trading analysis, especially to corroborate price breakouts, identify divergence, assess crowding, and avoid confusing volume tools with trend lines or oscillators. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat trading education and signal-confirmation guidance as financial advice or an automated trading system. <br>
Mitigation: Present outputs as analytical guidance only, require independent review before trading decisions, and do not connect the skill to trade execution or account-modifying tools. <br>
Risk: Volume and open-interest signals can be misleading when used without a prior price signal or when futures data is delayed, seasonal, or contract-specific. <br>
Mitigation: Use price action first, treat volume and open interest as corroborating evidence, prefer total market measures, and account for seasonal or contract-roll effects. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/bianchunhui/murphy-ta-skills/tree/main/volume-open-interest) <br>
- [ClawHub skill page](https://clawhub.ai/bianchunhui/skills/volume-open-interest) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance and structured trading-analysis rationale] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not execute code, place trades, fetch credentials, or modify accounts.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
