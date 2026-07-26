## Description: <br>
Paper-first live MLB moneyline evaluation and bounded Simmer execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kvzsolt](https://clawhub.ai/user/kvzsolt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and market operators use this skill to evaluate in-progress MLB full-game moneylines against Simmer/Polymarket prices, run paper-mode checks, and submit bounded live orders only after explicit opt-in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live mode can place capped real-money prediction-market orders. <br>
Mitigation: Run paper mode first and enable --live only after accepting the possibility of losing the capped funds. <br>
Risk: API keys and wallet material are sensitive credentials. <br>
Mitigation: Keep secrets in environment-managed storage and do not write them to config files. <br>
Risk: Disabling safeguards can weaken SDK context checks in live mode. <br>
Mitigation: Avoid --no-safeguards unless deliberately accepting the reduced checks; retain hard EV, exposure, price, spread, slippage, idempotency, and SDK preflight controls. <br>


## Reference(s): <br>
- [MLB Live Trader on ClawHub](https://clawhub.ai/kvzsolt/skills/mlb-live-trader) <br>
- [DISCLAIMER.md](DISCLAIMER.md) <br>
- [clawhub.json](clawhub.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python entrypoints, JSON status output, and configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paper mode is the default; live orders require explicit --live opt-in and a SIMMER_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
