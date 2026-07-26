## Description: <br>
Openclaw Ledger helps agents and operators create and verify a local hash-chained audit ledger of workspace changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agent operators, and workspace maintainers use this skill to initialize a local audit ledger, record workspace changes, verify chain integrity, inspect recent entries, export audit data, and preserve or restore ledger backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records workspace state in a local .ledger directory, which can become sensitive if tracked paths contain confidential filenames or hashes. <br>
Mitigation: Treat .ledger as sensitive operational data, exclude secrets where possible, and review workspace contents before recording or exporting audit data. <br>
Risk: Restore and protection commands can replace active ledger files or reset session baselines. <br>
Mitigation: Use restore and protect only after reviewing the command behavior, and test them in non-critical workspaces before relying on them for important audit records. <br>


## Reference(s): <br>
- [Openclaw Ledger on ClawHub](https://clawhub.ai/atlaspa/skills/openclaw-ledger) <br>
- [atlaspa publisher profile](https://clawhub.ai/user/atlaspa) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Terminal text, JSON exports, and JSONL ledger files written under .ledger.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3 and uses the Python standard library; writes ledger state, session snapshots, frozen backups, and optional exports in the target workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
