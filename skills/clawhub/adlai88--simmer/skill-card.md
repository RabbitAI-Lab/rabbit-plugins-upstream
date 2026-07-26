## Description: <br>
The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adlai88](https://clawhub.ai/user/adlai88) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to register agents with Simmer, practice prediction-market trading in $SIM, and graduate deliberately to Polymarket or Kalshi with explicit human verification and safety limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables prediction-market trading workflows that can involve real-money venues after explicit setup. <br>
Mitigation: Keep the default $SIM practice mode until the SDK, trading caps, stop-loss behavior, wallet flow, and real-money venue settings have been reviewed. <br>
Risk: $SIM practice fills are synthetic and may not reflect real spreads, venue fees, order-book depth, or partial fills. <br>
Mitigation: Use backtesting and real-venue paper mode with live=False before trading real money, then start with small trades that stay within dashboard limits. <br>
Risk: A configured API key allows an agent to interact with Simmer tooling. <br>
Mitigation: Provide SIMMER_API_KEY only to agents intended to use Simmer, keep credentials out of public output, and require human-side wallet linking before real-money execution. <br>


## Reference(s): <br>
- [Simmer homepage](https://simmer.markets) <br>
- [Simmer documentation](https://docs.simmer.markets) <br>
- [Full reference for agents](https://docs.simmer.markets/llms-full.txt) <br>
- [Simmer backtesting documentation](https://docs.simmer.markets/backtesting) <br>
- [Building Simmer strategy skills](https://docs.simmer.markets/skills/building) <br>
- [ClawHub skill page](https://clawhub.ai/adlai88/skills/simmer) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SIMMER_API_KEY for SDK use; TRADING_VENUE is optional and should remain unset or sim until real-money trading is explicitly enabled.] <br>

## Skill Version(s): <br>
1.24.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
