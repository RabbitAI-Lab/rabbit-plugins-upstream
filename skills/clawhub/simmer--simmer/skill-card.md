## Description: <br>
The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simmer](https://clawhub.ai/user/simmer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use Simmer to register an agent, start in virtual $SIM practice mode, and graduate to Polymarket or Kalshi trading only after explicit human verification and wallet setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security adjudication reports clean telemetry but notes local artifact inspection was unavailable. <br>
Mitigation: Confirm the packaged files and installation steps match the advertised Simmer purpose before release. <br>
Risk: Agents may trade real-money venues if the user graduates from practice mode and configures Polymarket or Kalshi. <br>
Mitigation: Keep the default virtual $SIM mode until human verification, wallet linking, trade caps, and venue selection are intentional. <br>
Risk: Virtual $SIM practice fills are synthetic and do not fully model real venue execution. <br>
Mitigation: Use real-venue paper mode or backtesting before risking capital, and account for spread, fees, and liquidity. <br>


## Reference(s): <br>
- [Simmer homepage](https://simmer.markets) <br>
- [Simmer documentation](https://docs.simmer.markets) <br>
- [Full reference for agents](https://docs.simmer.markets/llms-full.txt) <br>
- [Backtesting documentation](https://docs.simmer.markets/backtesting) <br>
- [Simmer ClawHub skill page](https://clawhub.ai/simmer/skills/simmer) <br>
- [Simmer publisher profile](https://clawhub.ai/user/simmer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python code, environment variables, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SIMMER_API_KEY; optional TRADING_VENUE can select polymarket or kalshi after explicit graduation from virtual practice mode.] <br>

## Skill Version(s): <br>
1.24.9 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
