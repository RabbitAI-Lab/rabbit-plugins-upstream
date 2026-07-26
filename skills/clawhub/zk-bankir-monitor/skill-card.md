## Description: <br>
Monitor a ZK-Bankir sovereign banking treasury via API for health checks, balance queries, decision ledger tracking, and hash-chain verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to let an agent query a ZK-Bankir server, summarize treasury health, inspect balances, monitor decisions, and verify ledger integrity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security review flagged under-disclosed write and server-admin capabilities in a financial monitoring workflow. <br>
Mitigation: Require explicit human confirmation before any POST request or local Rails runner action, and review commands before execution. <br>
Risk: The documented ZK-Bankir Phase 1 API has no authentication layer and uses plain HTTP. <br>
Mitigation: Use the skill only on localhost or a trusted internal network, and avoid real treasury or approval workflows until authentication and TLS are in place. <br>
Risk: The skill interacts with treasury, decision, and admin endpoints where incorrect assumptions could affect operational decisions. <br>
Mitigation: Treat agent output as monitoring guidance, verify critical balances and approvals in the source system, and keep human approval in place for financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1beekeeper/skills/zk-bankir-monitor) <br>
- [ZK-Bankir repository](https://gitlab.com/1Beekeeper/zk-bankir) <br>
- [ZK-Bankir documentation](https://gitlab.com/1Beekeeper/zk-bankir/-/tree/main/docs) <br>
- [De 10 Gebuden doctrine](https://gitlab.com/1Beekeeper/zk-bankir/-/blob/main/docs/02-doctrine.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and JSON API response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query localhost or a configured ZK_BANKIR_HOST and may require local ZK_BANKIR_PATH access for hash-chain verification.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
