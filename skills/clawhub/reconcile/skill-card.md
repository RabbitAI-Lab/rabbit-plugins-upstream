## Description: <br>
Tripwire check for multi-session drift. Scans state files, recent commits, and file conflicts caused by parallel Claude Code sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Reconcile after parallel Claude Code sessions, worktree merges, or crashes to inspect repository drift, file conflicts, state inconsistencies, and single-source-of-truth violations before approving fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects git history and project state files, which may expose sensitive repository context during review. <br>
Mitigation: Invoke it deliberately in sensitive repositories and limit review output sharing to authorized users. <br>
Risk: Proposed fixes for drift or conflicting state can be incorrect if session intent is ambiguous. <br>
Mitigation: Review each proposed fix before approving edits, using commit messages and related file changes to confirm intent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/reconcile) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with shell command snippets and proposed fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; proposed fixes require user approval before edits are applied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
