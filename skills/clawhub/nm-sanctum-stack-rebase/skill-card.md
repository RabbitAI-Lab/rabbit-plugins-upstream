## Description: <br>
Cascades a rebase through an entire PR stack after a base PR merges or upstream changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to update stacked pull request branches after a base branch changes, a root PR merges, or a mid-stack slice is revised. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad git and pull-request triggers may route ordinary repository requests into a stacked-branch rebase workflow. <br>
Mitigation: Use the skill only when an agent-assisted stacked-PR rebase is intended, and confirm the target stack, base branch, current repository, and remote state before proceeding. <br>
Risk: The workflow can rewrite branch history, force-push branches, and edit pull request bases. <br>
Mitigation: Review every `git push --force-with-lease`, `jj git push --all --allow-new`, and `gh pr edit` action before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-rebase) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and progress checklist items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides Git, jj, and GitHub CLI actions for rebasing and force-pushing stacked branches.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
