## Description:

Git版本管理工具 helps agents guide developers through Git command workflows for commits, branches, merge conflicts, remote synchronization, history review, rollback, rebasing, stashing, tags, submodules, and cleanup, with examples for Gitee and GitCode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they need an agent to explain or propose Git commands for daily version-control work, collaboration workflows, conflict resolution, history cleanup, and remote repository synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide destructive local or remote Git operations such as reset --hard, clean -fdx, branch or tag deletion, rebase, and force-push workflows.

Mitigation: Require manual confirmation for every mutating command and verify the target repository, branch, commit, and backup or recovery path before execution.

Risk: The artifact under-discloses command-execution risk for workflows that can overwrite history or remove files.

Mitigation: Present high-impact Git commands as reviewable proposals and prefer reversible commands, dry runs, or safer alternatives such as revert and --force-with-lease where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-essentials)
- [SkillHub homepage](https://skillhub.cn/skill/)
- [Git official documentation](https://git-scm.com/doc)
- [Pro Git book](https://git-scm.com/book)
- [A Visual Git Reference](https://marklodato.github.io/visual-git-guide/)
- [Gitee Help Center](https://gitee.com/help)
- [GitCode documentation](https://gitcode.com/docs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are proposals and guidance for Git workflows; mutating operations require user review before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
