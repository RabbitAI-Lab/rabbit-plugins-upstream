## Description: <br>
Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for concurrent reviews or feature work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to manage isolated Git worktrees for parallel development, code review, branch switching, and cleanup workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may copy .env files containing API keys, production credentials, customer data, or other secrets into additional local worktree directories. <br>
Mitigation: Review before installing in sensitive repositories and prefer an opt-in secret-copy step or per-worktree secret provisioning. <br>
Risk: The skill may mutate repository state during normal use, including updating .gitignore and creating or removing local worktree directories. <br>
Mitigation: Review the repository changes after worktree operations and confirm cleanup actions before removing worktrees. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree) <br>
- [Workflow Examples](references/workflow-examples.md) <br>
- [Troubleshooting & Technical Details](references/troubleshooting.md) <br>
- [Hooks and Local Excludes](references/hooks-and-excludes.md) <br>
- [Worktree Manager Script](scripts/worktree-manager.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run the bundled worktree manager script and summarize worktree status or next actions.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
