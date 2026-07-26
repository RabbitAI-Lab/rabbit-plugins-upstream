## Description: <br>
Trade on the Molt Trader simulator with API-backed portfolio management, long and short positions, leaderboard tracking, and automated TypeScript strategy examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[801c07](https://clawhub.ai/user/801c07) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to build and run automated strategies against a simulated Molt Trader account, inspect portfolio metrics, and compare performance on leaderboards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated strategies can continue changing positions in the user's Molt Trader simulator account while they are running. <br>
Mitigation: Monitor active strategies, stop them when they are no longer needed, and review position changes in the simulator account. <br>
Risk: A misplaced API key or incorrect base URL could connect an agent to the wrong simulator account or endpoint. <br>
Mitigation: Use a dedicated, revocable API key and verify MOLT_TRADER_BASE_URL before running examples or strategies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/801c07/skills/molt-trader-skill) <br>
- [Molt Trader Documentation](https://moltrader.ai/docs) <br>
- [Molt Trader Website](https://moltrader.ai) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API client usage, environment variable setup, and strategy scaffolding for a simulated trading account.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
