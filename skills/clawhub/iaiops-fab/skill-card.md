## Description: <br>
Fab edition of iaiops for semiconductor and display fab equipment, covering SECS/GEM, SECS-II, HSMS, GEM host workflows, OPC-UA equipment-control data, downtime root-cause support, OEE, asset inventory, and data quality with a read-first posture and MOC-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and fab operations engineers use this skill to inspect SECS/GEM and OPC-UA equipment signals, triage downtime and alarms, evaluate OEE and data quality, and prepare controlled changes through MOC-gated workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes high-impact industrial write and data export capabilities in a fab-operations context. <br>
Mitigation: Review the actual iaiops[fab] runtime before production installation and confirm write tools are technically blocked unless MOC approval, dry-run review, undo capture, and named approver checks are enforced. <br>
Risk: Fab data exports or publishing workflows may expose sensitive operational data. <br>
Mitigation: Restrict export and publish destinations for sensitive fab data before enabling the skill in production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first operational guidance; any write-path recommendations should preserve dry-run review, undo capture, and named approver checks.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
