## Description: <br>
Verifies workspace state and staged changes as a preflight before commits or PRs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect repository status, staged changes, and diffs before commit, pull request, or release-note workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary says the skill claims to be read-only while instructing agents to stage or unstage files, run Makefile targets, and fix files. <br>
Mitigation: Require explicit confirmation before staging, unstaging, formatting, linting, merge-abort, make commands, or file edits. <br>
Risk: The security verdict is suspicious for normal use because the skill can move from repository inspection into modifying the workspace. <br>
Mitigation: Install only when that behavior is intended, and narrow triggers or edit the skill if a truly read-only review helper is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-git-workspace-review) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include git status, diff statistics, detailed diff review notes, and code-quality check results.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
