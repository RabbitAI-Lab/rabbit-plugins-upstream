## Description: <br>
AgentGit validates and merges multi-agent git work through a deterministic gate that requires a real validation command to exit 0 before merge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tryboy869](https://clawhub.ai/user/tryboy869) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use AgentGit to validate sub-agent changes with project-specific automated checks and merge only approved work into a git repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an external AgentGit CLI that can merge repository changes. <br>
Mitigation: Review the AgentGit repository, pin a trusted commit or release, and use it only where automated validation and branch merges are acceptable. <br>
Risk: A stale or inappropriate validation command could approve changes that do not satisfy the user's task. <br>
Mitigation: Confirm task approval is fresh and require a project-specific validation command to pass before running merge. <br>


## Reference(s): <br>
- [ClawHub AgentGit listing](https://clawhub.ai/tryboy869/skills/agentgit) <br>
- [AgentGit protocol](https://github.com/Tryboy869/AgentGit/blob/main/docs/en/protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and git; validation and merge commands operate in the user's git repository.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
