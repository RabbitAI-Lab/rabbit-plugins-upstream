## Description: <br>
Scan for orphaned worktrees and stale branches after crashes or abandoned sessions. Offers safe cleanup options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to inspect git worktrees, branches, and prunable state after crashes, abandoned sessions, or periodic repository hygiene checks. It reports findings first and requires explicit approval before cleanup actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup commands can remove worktrees, delete branches, prune refs, merge branches, or cherry-pick commits. <br>
Mitigation: Run the scan first, review exact proposed targets and reasons, and approve only the specific cleanup actions you intend to perform. <br>
Risk: A worktree with unknown activity could be mistaken for abandoned work. <br>
Mitigation: Treat recent or ambiguous worktrees as possibly live unless lock, heartbeat, process, and file-state evidence supports cleanup. <br>
Risk: Unmerged commits or uncommitted changes could be lost if stale branches or worktrees are discarded. <br>
Mitigation: Preserve work by reviewing status, recent commits, and default-branch differences before choosing merge, cherry-pick, or deletion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/recover) <br>
- [Publisher profile](https://clawhub.ai/user/conorbronsdon) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only scan report by default; cleanup commands are proposed for user approval before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
