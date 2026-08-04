## Description: <br>
Git repository and SourceGit integration for cloning with ghq, managing worktrees, converting repository layouts, handling multi-account authentication, and staging isolated changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to manage Git repositories, worktrees, SourceGit registration, ghq migrations, multi-account SSH or HTTPS credentials, and isolated staging workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide active Git maintenance rather than only reading repository state. <br>
Mitigation: Install it only for workflows where an agent is expected to manage repositories, worktrees, migrations, staging, pushes, and PR preparation. <br>
Risk: Some workflows involve sensitive GitHub tokens or credential configuration. <br>
Mitigation: Prefer safer Git credential helpers, avoid token-in-URL clone paths, and review any credential-helper or SSH mapping changes before use. <br>
Risk: The skill may propose persistent local changes such as SourceGit preference edits, global gitconfig changes, directory deletion, push, or PR creation. <br>
Mitigation: Require explicit confirmation before applying persistent configuration changes, deleting directories, pushing branches, or creating pull requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>
- [SKILL](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local Git, ghq, SourceGit, SSH, credential-helper, filesystem, push, and PR operations depending on the selected topic.] <br>

## Skill Version(s): <br>
0.7.0 (source: ClawHub release evidence and CHANGELOG, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
