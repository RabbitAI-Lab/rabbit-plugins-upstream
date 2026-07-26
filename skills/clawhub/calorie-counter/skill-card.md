## Description: <br>
Track daily calorie and protein intake, set goals, and log weight using local SQLite storage with automatic daily totals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cnqso](https://clawhub.ai/user/cnqso) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to log foods, calorie goals, protein intake, and weight measurements through an agent-assisted local tracker. It is intended for personal tracking workflows where local plaintext SQLite storage is acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Food, calorie, protein, goal, and weight history are saved in a persistent local SQLite database. <br>
Mitigation: Use the skill only in a private local workspace and avoid shared or synced folders unless plaintext health-related tracking data is acceptable there. <br>
Risk: Broad food mentions may lead an agent to log entries automatically. <br>
Mitigation: Tell the agent to add food or weight records only after explicit confirmation, and review or delete mistaken entries with the list and delete commands. <br>


## Reference(s): <br>
- [Calorie Counter Skill Page](https://clawhub.ai/cnqso/skills/calorie-counter) <br>
- [cnqso Publisher Profile](https://clawhub.ai/user/cnqso) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text summaries with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores calorie, protein, goal, and weight history in a local SQLite database.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
