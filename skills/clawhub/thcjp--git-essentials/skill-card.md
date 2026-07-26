## Description: <br>
Git Essentials guides agents through Git command-line workflows for repository setup, commits, branching, merges, remote synchronization, history inspection, resets, rebases, stashes, tags, submodules, cleanup, and common error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to ask an agent for Git command guidance, workflow steps, and troubleshooting help for everyday commits, branch collaboration, conflict resolution, releases, and history cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Destructive Git examples can discard local work or rewrite repository history if executed without review. <br>
Mitigation: Confirm the target repository, branch, remote, and intent before running reset hard, clean, branch deletion, tag deletion, or force-with-lease commands. <br>
Risk: Command guidance applied to the wrong repository or remote can affect unrelated code or collaborators. <br>
Mitigation: Check git status, current branch, and configured remotes before allowing an agent to run synchronization, deletion, or history-changing commands. <br>


## Reference(s): <br>
- [Git Documentation](https://git-scm.com/doc) <br>
- [Pro Git Book](https://git-scm.com/book) <br>
- [A Visual Git Reference](https://marklodato.github.io/visual-git-guide/) <br>
- [Gitee Help Center](https://gitee.com/help) <br>
- [GitCode Documentation](https://gitcode.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Git command snippets and workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that modify repository history or delete local work; review the target repository and command impact before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
