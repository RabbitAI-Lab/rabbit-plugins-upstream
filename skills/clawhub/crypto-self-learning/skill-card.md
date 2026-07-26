## Description: <br>
Self-learning system for crypto trading that logs trades with context, analyzes win/loss patterns, and updates learned trading rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[totaleasy](https://clawhub.ai/user/totaleasy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and trading agents use this skill to record crypto trades, analyze local trading history, generate data-driven rules, and optionally update agent memory with learned patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist user-provided trade history and learned rules locally. <br>
Mitigation: Keep trade logs free of secrets, exchange credentials, and other sensitive account details. <br>
Risk: Generated trading rules may reflect incomplete or low-sample trade history. <br>
Mitigation: Review analysis outputs before relying on them for trading decisions. <br>
Risk: The memory update script can modify a user-supplied MEMORY.md file. <br>
Mitigation: Preview updates with dry-run behavior or require explicit approval before writing memory changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/totaleasy/skills/crypto-self-learning) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, terminal summaries, and JSON-backed local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local trade records, learned rule JSON, analysis summaries, and optional MEMORY.md updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
