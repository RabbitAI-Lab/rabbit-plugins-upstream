## Description: <br>
DOGE节点免费版 helps Dogecoin Core node operators inspect node status, wallet balances, transaction history, unspent outputs, receiving addresses, and basic RPC/configuration guidance through dogecoin-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators running a local Dogecoin Core full node use this skill to check synchronization, peer connectivity, wallet balances, transactions, unspent outputs, and receiving-address workflows. It formats dogecoin-cli/RPC-oriented results and provides configuration guidance for node operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence marks the release suspicious because it requests command and write authority while giving inconsistent boundaries around wallet-changing and export-like operations. <br>
Mitigation: Review before installing when the agent can access a real Dogecoin wallet, restrict use to local Dogecoin Core node and wallet inspection, and require explicit confirmation before creating addresses, exporting data, editing configuration, or touching wallet state. <br>
Risk: Generic analytics-style trigger language in the artifact could cause use outside the Dogecoin node-management scope. <br>
Mitigation: Use the skill only for Dogecoin Core node and wallet inspection workflows described in the release evidence. <br>
Risk: RPC credentials and local wallet data are sensitive. <br>
Mitigation: Keep RPC bound to localhost, avoid hardcoding credentials in skill files or scripts, and review generated shell commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/doge-node-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, tables, JSON-shaped result examples, shell command snippets, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local Dogecoin Core node and dogecoin-cli; some workflows may inspect wallet state or create receiving addresses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
