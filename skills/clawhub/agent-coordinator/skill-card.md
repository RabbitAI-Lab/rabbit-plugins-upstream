## Description: <br>
Multi-agent coordination protocol for task distribution, result aggregation, and parallel execution across multiple AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decompose tasks, run parallel or sequential coordination patterns, aggregate results, and produce ensemble votes for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The coordinator can read a JSON file path supplied with --subtasks. <br>
Mitigation: Use trusted subtask files and avoid pointing the command at sensitive local files. <br>
Risk: The coordinator can write a JSON results file path supplied with --export. <br>
Mitigation: Choose an intended output path in a working directory and avoid overwriting important files. <br>
Risk: Coordination results can be incomplete or misleading if the proposed subtasks or votes are accepted without review. <br>
Mitigation: Review generated subtasks, summaries, and ensemble results before using them for decisions or downstream work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/agent-coordinator) <br>
- [Publisher profile](https://clawhub.ai/user/chen6896qqwee) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text status output or JSON result objects, with optional JSON export files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3. Can read user-supplied JSON subtask files and write user-specified JSON export files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
