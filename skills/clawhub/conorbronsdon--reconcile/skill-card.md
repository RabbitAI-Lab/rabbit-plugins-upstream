## Description: <br>
Tripwire check for multi-session drift. Scans state files, recent commits, and file conflicts caused by parallel Claude Code sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to check for repository drift after parallel Claude Code sessions, worktree merges, crashes, or heavy multi-branch work. It reports branch conflicts, state drift, SSOT violations, and proposed fixes for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads git history, branch diffs, and project state files in the current repository. <br>
Mitigation: Install it only in repositories where that read access is acceptable. <br>
Risk: Proposed fixes for complex merges or parallel worktree activity may not reflect the user's intended resolution. <br>
Mitigation: Review each proposed fix before approving any file changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/reconcile) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with shell command snippets and proposed fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; file changes are proposed for user approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
