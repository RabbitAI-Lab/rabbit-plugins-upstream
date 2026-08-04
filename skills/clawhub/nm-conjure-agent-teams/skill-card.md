## Description: <br>
Coordinates Claude agent teams via filesystem protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to coordinate multiple Claude Code agents on parallel implementation, review, refactoring, testing, and task-management workflows that benefit from explicit team roles, dependencies, and inbox-based coordination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start, stop, and replace Claude agent processes. <br>
Mitigation: Use it only for explicit agent-team workflows and require manual confirmation before shutdown, replacement, force-kill, or recovery actions. <br>
Risk: The skill can create and delete persistent coordination state under ~/.claude/teams and ~/.claude/tasks. <br>
Mitigation: Review or back up team and task directories before cleanup or deletion, and limit deletion to named teams the operator intends to remove. <br>
Risk: Parallel agents may make conflicting or unsafe workspace changes if roles, task ownership, and risk tiers are not enforced. <br>
Mitigation: Assign clear file ownership, use role and risk-tier gates for higher-risk work, prefer worktree isolation when agents modify files, and review diffs and tests before integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-agent-teams) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON structures and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may result in local team and task state under ~/.claude and separate Claude processes launched through tmux or equivalent terminal panes.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
