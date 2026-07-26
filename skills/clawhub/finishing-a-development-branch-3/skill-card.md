## Description: <br>
Guides an agent through finalizing completed development work by verifying tests and presenting structured options for merge, pull request, preservation, or discard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill when implementation is complete and tests pass to choose and carry out a safe branch finishing workflow: local merge, pull request, preservation, or discard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real Git operations, including merges, pushes, branch deletion, and worktree removal. <br>
Mitigation: Use it only in repositories where those changes are acceptable, review the branch and worktree details, and require explicit confirmation before discard or cleanup. <br>
Risk: Proceeding with failing tests could merge or publish broken work. <br>
Mitigation: The workflow requires test verification before offering branch completion options and again after a local merge. <br>
Risk: Worktree cleanup can remove an actively used workspace if ownership is misidentified. <br>
Mitigation: The workflow only removes worktrees under known .worktrees/ or worktrees/ paths and otherwise preserves externally managed workspaces. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/ivansslo/Supwrs/tree/main/skills/finishing-a-development-branch) <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/finishing-a-development-branch-3) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured option prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the agent to verify tests, inspect Git state, and request explicit confirmation before destructive cleanup.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
