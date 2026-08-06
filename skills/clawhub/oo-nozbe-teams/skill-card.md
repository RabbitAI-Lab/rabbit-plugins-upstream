## Description: <br>
Nozbe (nozbe.com) skill for reading, creating, updating, and deleting Nozbe data instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with their connected Nozbe account for team, project, task, and comment workflows. It supports read operations as well as user-confirmed create, update, and delete operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Nozbe projects, tasks, and comments through a connected account. <br>
Mitigation: Review exact payloads and effects before approving write actions, and require explicit approval before destructive actions. <br>
Risk: The skill uses the user's connected OOMOL/Nozbe account, so actions may affect real workspace data. <br>
Mitigation: Install and use it only when agent access to the connected Nozbe account is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nozbe-teams) <br>
- [Nozbe homepage](https://nozbe.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from connector runs are JSON objects with data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
