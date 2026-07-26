## Description: <br>
自动分析代码变更并生成符合规范的 Git Commit。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linuxcer](https://clawhub.ai/user/linuxcer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Git changes, generate a Conventional Commits-style message, and create a repository commit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may automatically stage all files and create a Git commit without a clear confirmation step. <br>
Mitigation: Use it only in repositories where agent-driven Git state changes are acceptable, prefer already-staged commits, and require explicit approval after reviewing the files, diff summary, branch, and commit message. <br>
Risk: Automatic `git add .` can include unintended files in a commit. <br>
Mitigation: Review the status and staged diff before committing, and stage files manually when the commit scope needs to be constrained. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linuxcer/git-commit-helper) <br>
- [Commit Format Reference](artifact/references/commit-format.md) <br>
- [Safety and Error Handling Reference](artifact/references/safety-errors.md) <br>
- [Workflow Examples Reference](artifact/references/workflow-examples.md) <br>
- [Best Practices Reference](artifact/references/best-practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline Git shell commands and commit messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute Git staging and commit operations when used by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
