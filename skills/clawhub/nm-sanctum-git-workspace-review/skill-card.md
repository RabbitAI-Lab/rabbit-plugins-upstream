## Description: <br>
Verifies workspace state and staged changes as a preflight before commits or PRs to confirm the staged set is clean and correct. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before commits, pull requests, or release-note preparation to inspect repository status, staged and unstaged diffs, and the intended change set. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is described as read-only but includes steps that can change staging state or rewrite repository files through formatting and lint-fix workflows. <br>
Mitigation: Use it only when repository changes are intended, and require explicit user approval before staging, unstaging, formatting, linting, or fixing files. <br>
Risk: Git diff and status guidance can expose sensitive uncommitted code or local file names in agent output. <br>
Mitigation: Review the repository context before sharing output outside the workspace and avoid pasting confidential diffs into external channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-git-workspace-review) <br>
- [metadata.clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [modules/git-commands.md](modules/git-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include repository status summaries, staged or unstaged diff observations, and recommended next actions.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
