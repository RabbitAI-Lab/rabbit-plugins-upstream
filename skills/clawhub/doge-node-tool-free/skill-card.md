## Description: <br>
DOGE节点免费版 helps agents operate against a local Dogecoin Core node by wrapping common dogecoin-cli status, wallet, transaction, address, RPC reference, and configuration tasks into readable guidance and structured outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Dogecoin node operators and agent-assisted infrastructure users use this skill to inspect node sync status, peer/network state, local wallet balances, recent transactions, unspent outputs, and basic Dogecoin Core RPC usage. It is intended for local Dogecoin Core environments where the agent may propose or run dogecoin-cli commands and summarize their results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide or run local commands against a Dogecoin Core node and wallet, including commands that reveal wallet balances, transactions, unspent outputs, or generate new receiving addresses. <br>
Mitigation: Restrict invocation to explicit Dogecoin Core and dogecoin-cli tasks, review proposed shell commands before execution, and require confirmation before generating addresses or handling wallet backup/export data. <br>
Risk: Wallet results and callback-style outputs may expose sensitive local wallet information if sent to an untrusted destination. <br>
Mitigation: Keep wallet outputs local unless the destination is trusted, and avoid callback URLs for wallet-related results unless their ownership and transport security are clear. <br>
Risk: The release security summary notes ambiguity between read-only claims and capabilities that can access wallet data and run local commands. <br>
Mitigation: Treat the skill as requiring review before deployment, constrain allowed operations to expected read-oriented queries, and confirm any non-query or wallet-affecting action with the user. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/thcjp/skills/doge-node-tool-free) <br>
- [Skill definition artifact](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, JSON examples, bash command snippets, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured status summaries, execution logs, Dogecoin Core RPC command examples, and dogecoin.conf guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and target metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
