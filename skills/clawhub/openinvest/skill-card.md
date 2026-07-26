## Description: <br>
openInvest helps agents monitor multi-asset investment portfolios, review live prices and strategy history, adjust positions, and run a four-role LLM investment committee for asset verdicts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[longsizhuo](https://clawhub.ai/user/longsizhuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use openInvest for daily portfolio monitoring, market-price checks, strategy and decision-history review, asset tracking, trade logging, and investment committee analysis before making investment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private portfolio records, wealth context, local investment history, and committee transcripts. <br>
Mitigation: Install only when that data access is acceptable, use a dedicated INVEST_HOME data directory, and review stored data under INVEST_HOME and memory/.committee. <br>
Risk: The skill can mutate portfolio records, trade-status records, configuration, and remote-hub state. <br>
Mitigation: Require explicit user confirmation before buy, sell, deposit, withdraw, record-execution, config, or remote-hub write operations. <br>
Risk: The skill may collect or rely on LLM, email, or remote-hub credentials. <br>
Mitigation: Avoid pasting secrets into chat and store credentials only in the intended local or hub configuration locations. <br>


## Reference(s): <br>
- [openInvest ClawHub Skill Page](https://clawhub.ai/longsizhuo/skills/openinvest) <br>
- [Full Skill Protocol](SKILL.md) <br>
- [Project Architecture Wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki) <br>
- [Committee Protocol](references/committee-protocol.md) <br>
- [Committee Protocol - Hermes and Delegating Agents](references/committee-protocol-hermes.md) <br>
- [Dual Execution Paths](references/two-paths.md) <br>
- [Tool Catalog](references/tools.md) <br>
- [Adding a New Asset](references/adding-assets.md) <br>
- [Onboarding](references/onboarding.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON or Markdown backend outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read private portfolio state and may guide CLI or MCP operations that mutate local or remote investment records.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release metadata, SKILL.md frontmatter, CHANGELOG.md released 2026-07-17) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
