## Description: <br>
Provides concise guidance for advanced Git workflows, including commits, rebase, bisect, worktrees, reflog recovery, cherry-pick, submodules, subtrees, and pull request flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cooperiano](https://clawhub.ai/user/cooperiano) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a compact reference for higher-impact Git operations and branch-management workflows. It is most useful when preparing commits, rebasing personal branches, recovering with reflog, coordinating worktrees, or managing pull request updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested rebase, amend, cherry-pick, or force-with-lease workflows can rewrite history or affect the wrong branch if applied without review. <br>
Mitigation: Use these workflows on personal branches, confirm the target branch and remote before pushing, and avoid rewriting shared history without team agreement. <br>
Risk: Concise command guidance can omit repository-specific policy or review requirements. <br>
Mitigation: Review proposed Git commands against the repository's contribution rules and scan changes before deployment or pull request submission. <br>


## Reference(s): <br>
- [Git Pro on ClawHub](https://clawhub.ai/cooperiano/skills/git-pro) <br>
- [cooperiano publisher profile](https://clawhub.ai/user/cooperiano) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Concise Git workflow guidance; no files, code execution, persistence, or external API calls are produced by the skill itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
