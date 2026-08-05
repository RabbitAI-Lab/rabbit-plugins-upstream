## Description: <br>
Recovers broken agent state via crash recovery, context overflow, and merge conflict protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to recover interrupted or inconsistent agent sessions by triaging crashes, context loss, merge conflicts, and mismatched task, git, and disk state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as state and context may invoke the skill when recovery is not intended. <br>
Mitigation: Use it only when an agent needs to inspect or repair a broken worktree or interrupted session. <br>
Risk: Recovery procedures can change local git state through stash, commit, restore, or abort actions. <br>
Mitigation: Review proposed git actions before allowing the agent to execute them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-damage-control) <br>
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown with inline shell commands and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Procedural recovery guidance for local worktree and session-state repair.] <br>

## Skill Version(s): <br>
1.9.17 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
