## Description: <br>
Provides agent-facing guidance for advanced Git workflows, including interactive rebase, bisect, worktree, reflog recovery, and cherry-pick operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and execute advanced Git operations such as cleaning commit history, finding regression-introducing commits, working across multiple branches, and recovering from mistaken Git actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advanced Git commands suggested by the skill can rewrite history, remove worktrees, or discard local changes if run in the wrong repository state. <br>
Mitigation: Before accepting commands, run git status, save or stash local work, create a backup branch for recovery operations, and review destructive commands such as reset --hard, rebase, cherry-pick, and worktree remove --force. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-workflows-tool-free) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command sequences that require human review before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
