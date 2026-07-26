## Description: <br>
Check the user's coding-agent leaderboard - token usage, cost, and rank among friends across Claude Code, Codex, OpenCode, Amp, and pi-agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mazzzystar](https://clawhub.ai/user/mazzzystar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding-agent users use this skill to check token usage, estimated AI spend, and leaderboard rank across ccclub groups, and to set up or join a shared leaderboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead users to share aggregated coding-agent usage and cost metadata with ccclub and leaderboard group members. <br>
Mitigation: Review the privacy expectation before setup and run `ccclub show-data` to inspect exactly what is uploaded. <br>
Risk: Setup commands install background sync automatically. <br>
Mitigation: Confirm the user wants ongoing sync before setup, and consult the CLI documentation to disable or remove syncing when it is no longer desired. <br>


## Reference(s): <br>
- [ClawHub Ccclub listing](https://clawhub.ai/mazzzystar/skills/ccclub) <br>
- [ccclub API notes](https://ccclub.dev/llms.txt) <br>
- [ccclub read-only leaderboard API](https://ccclub.dev/api/rank/{groupCode}?period=daily&tz={utcOffsetMinutes}) <br>
- [ccclub group dashboard](https://ccclub.dev/g/<CODE>) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide the agent to inspect ccclub JSON output, compare leaderboard rows, and run setup or sync commands.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
