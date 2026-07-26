## Description: <br>
Trade K-pop lightstick tokens on a bonding curve market using artist popularity, news trends, and price signals to guide buy and sell decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hans1329](https://clawhub.ai/user/hans1329) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and trading-agent operators use this skill to inspect K-pop lightstick token prices, popularity signals, and news context, then prepare buy or sell calls for the K-Trendz bonding curve market. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Buy and sell calls may execute real token trades and cause financial loss. <br>
Mitigation: Require explicit per-trade approval, spending limits, and price and risk checks before allowing an agent to call trading tools. <br>
Risk: The skill can affect funds without enough visible consent and risk guardrails. <br>
Mitigation: Review the skill before installing and restrict automated use to accounts and API keys with bounded daily volume and transaction limits. <br>
Risk: Authenticated API requests require a bot API key. <br>
Mitigation: Store the API key securely and avoid exposing it in prompts, logs, generated examples, or shared outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hans1329/skills/clawhub-skills) <br>
- [K-Trendz bot API base URL](https://jguylowswwgjvotdcsfj.supabase.co/functions/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Code] <br>
**Output Format:** [Markdown with JSON request and response examples plus Python pseudocode] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare authenticated token-price, buy, and sell requests; trade execution should remain subject to explicit approval and risk limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
