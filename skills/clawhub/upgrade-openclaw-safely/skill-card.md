## Description: <br>
Use when upgrading OpenClaw or recovering from partial updates, gateway failures, migrations, service drift, channel failures, or version mismatch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skillmelody](https://clawhub.ai/user/skillmelody) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to plan, apply, verify, and recover OpenClaw upgrades with supervised approvals, transaction state, backup checks, bounded service reconciliation, and stability evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through real OpenClaw upgrades and service recovery, which may affect a live installation if the user approves mutation. <br>
Mitigation: Use supervised authority only, require explicit approval for apply, recovery, rollback, and each service action, and verify backups before core mutation. <br>
Risk: A repeated or blind update attempt after a partial failure could overwrite useful evidence or worsen recovery. <br>
Mitigation: Use the transaction guard to limit each run to one core update attempt, classify failures, preserve evidence, and resume from recorded state. <br>
Risk: Readiness can be mistaken for completion when a gateway reports ready once but later restarts or loses routes. <br>
Mitigation: Require at least three observations spanning 120 seconds with stable process identity, passing readiness layers, and no source=update delta before reporting success. <br>


## Reference(s): <br>
- [Transaction Contract](artifact/references/transaction-contract.md) <br>
- [Recovery Contract](artifact/references/recovery-contract.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/skillmelody/skills/upgrade-openclaw-safely) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON transaction records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled guard records state and authorization decisions but does not execute OpenClaw, service manager, recovery, rollback, or cleanup commands.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
