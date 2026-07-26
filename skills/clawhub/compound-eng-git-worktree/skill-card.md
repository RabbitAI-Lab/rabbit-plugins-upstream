## Description: <br>
Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for concurrent reviews or feature work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to manage isolated Git worktrees for parallel implementation, branch review, and cleanup workflows without switching the main working tree in place. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper can duplicate local .env files containing secrets into newly created worktrees. <br>
Mitigation: Review or edit the helper before use on repositories with real credentials, require opt-in or an allowlist for env copying, prefer .env.example, and verify copied env files stay ignored and are cleaned up with discarded worktrees. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree) <br>
- [Workflow Examples](references/workflow-examples.md) <br>
- [Troubleshooting & Technical Details](references/troubleshooting.md) <br>
- [Hooks and Local Excludes](references/hooks-and-excludes.md) <br>
- [Worktree Manager Script](scripts/worktree-manager.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run Git worktree helper commands and may summarize branch, worktree, and cleanup status.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
