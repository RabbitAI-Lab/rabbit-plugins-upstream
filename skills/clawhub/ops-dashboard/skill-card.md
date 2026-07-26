## Description: <br>
Gather operational signals including disk usage, git status, recent commits, and resource metrics so an agent can summarize workspace health without manually running multiple checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to check workspace health before deployments, updates, or support work. It helps an agent summarize disk capacity, git state, recent commits, load averages, and large workspace directories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard output may expose local workspace health details such as git status, recent commits, changed file paths, directory names and sizes, disk usage, and system load. <br>
Mitigation: Run it only against workspaces where that metadata is appropriate for the agent and downstream readers to see. <br>
Risk: Pointing the dashboard at a broad or sensitive path can reveal more local project structure than intended. <br>
Mitigation: Use the --workspace option to scope checks to the intended repository or workspace. <br>


## Reference(s): <br>
- [Ops Dashboard reference](references/ops-dashboard.md) <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/ops-dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI report with Markdown command examples and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports local workspace and git metadata; no network sharing or persistence is indicated by the security evidence.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
