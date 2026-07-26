## Description: <br>
Create an anonymous Starknet wallet via Typhoon and interact with Starknet contracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[esdras-sena](https://clawhub.ai/user/esdras-sena) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agents use this skill to create or load a Starknet account through Typhoon, inspect Starknet contract ABIs, perform reads and authorized writes, execute AVNU swaps, and configure event watchers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local Starknet wallet keys and sign mainnet transactions. <br>
Mitigation: Use a fresh low-value wallet, set a trusted RPC endpoint, and inspect every transaction plan before confirming any write or swap. <br>
Risk: Scheduled event watchers can create persistent cron entries. <br>
Mitigation: Review watcher configuration before enabling schedules and check crontab plus ~/.openclaw/secrets/starknet after using scheduled watchers. <br>
Risk: Webhook integrations can send event data to external URLs. <br>
Mitigation: Avoid untrusted webhook URLs and only configure endpoints you control. <br>


## Reference(s): <br>
- [ArgentX Account Class Hashes](references/argentx-class-hashes.md) <br>
- [Typhoon Finance App](https://www.typhoon-finance.com/app) <br>
- [Argent Contracts Starknet](https://github.com/argentlabs/argent-contracts-starknet) <br>
- [Starkscan ArgentX Class Explorer](https://starkscan.co/class/0x036078334509b514626504edc9fb252328d1a240e4e948bef8d0c08dff45927f) <br>
- [Loot Survivor Contracts](https://docs.provable.games/lootsurvivor/contracts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON script inputs and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce transaction plans, account creation guidance, event watcher configuration, and JSON command outputs for Starknet operations.] <br>

## Skill Version(s): <br>
0.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
