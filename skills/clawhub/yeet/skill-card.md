## Description: <br>
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patrick-erichsen-2](https://clawhub.ai/user/patrick-erichsen-2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill when they want an agent to prepare a Git branch for review by staging changes, making a conventional commit, pushing to origin, and opening a draft GitHub pull request with the GitHub CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can broadly stage, commit, push, and open a GitHub pull request with limited scoping safeguards. <br>
Mitigation: Review `git status` and the exact diff before use, and run it only in repositories where publishing all staged and untracked changes is intended. <br>
Risk: The workflow may create branches, install dependencies, push to origin, and create draft pull requests. <br>
Mitigation: Use it only when those repository side effects are expected and the GitHub CLI session is authenticated for the intended account and repository. <br>


## Reference(s): <br>
- [Yeet ClawHub Skill Page](https://clawhub.ai/patrick-erichsen-2/skills/yeet) <br>
- [Patrick Erichsen ClawHub Profile](https://clawhub.ai/user/patrick-erichsen-2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and pull request description prose] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GitHub CLI authentication, repository git state, branch naming, conventional commit messages, and draft pull request creation.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
