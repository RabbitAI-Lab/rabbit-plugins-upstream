## Description: <br>
Automates GitHub contribution workflows by helping agents find suitable issues, prepare fork branches, plan fixes, and assemble pull request evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linux2010](https://clawhub.ai/user/linux2010) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to structure open source contribution work, including issue selection, fork synchronization, branch creation, change planning, proof collection, and pull request preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can reset or clean a repository and may discard local changes or files. <br>
Mitigation: Use it only in fresh or disposable clones, or after backing up or stashing local work; verify the project directory, remotes, branch, and git status before cleanup. <br>
Risk: The workflow can push synchronized changes to a fork without enough warning. <br>
Mitigation: Review the target owner, repository, origin, and upstream before execution, and require explicit confirmation before pushes. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/linux2010/skills/github-contribution) <br>
- [GitHub contribution workflow](artifact/github-contribution-workflow.md) <br>
- [Live-proof cases](artifact/live-proof-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, checklists, and pull request evidence templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Git commands that should be reviewed before execution in a local repository.] <br>

## Skill Version(s): <br>
1.7.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
