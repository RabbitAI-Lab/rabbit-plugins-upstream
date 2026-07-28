## Description: <br>
Schedule, inspect, retry, pause, resume, stop, and decommission unattended Codex CLI jobs through native macOS, Linux, or Windows schedulers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create and manage unattended Codex CLI jobs that run later or recur through the host operating system's scheduler. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled jobs can run later or recur under the user's local Codex login, approval, sandbox, and organization policy settings. <br>
Mitigation: Review each job's prompt, working directory, schedule, profile and config overrides, captured environment variables, and retention settings before creating it. <br>
Risk: Write-capable direct jobs may conflict with other jobs using the same working directory. <br>
Mitigation: Prefer worktree mode for recurring jobs that may write files, and avoid scheduling concurrent direct jobs against the same directory. <br>
Risk: Captured environment values and run artifacts are stored in local scheduler state and are not encrypted on disk. <br>
Mitigation: Avoid capturing secrets unless necessary, keep state under the private Codex state directory, and configure retention or prune old runs when appropriate. <br>


## Reference(s): <br>
- [Operational Semantics](references/semantics.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/wufei-png/skills/codex-native-scheduler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may lead the agent to create native scheduled Codex jobs and local scheduler state when the bundled CLI is executed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and scripts/codex_scheduler/__init__.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
