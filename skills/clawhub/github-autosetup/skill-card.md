## Description:

Automates GitHub and git setup for coding agents through Git Bash, including environment probing, HTTPS/GCM or SSH transport selection, browser OAuth, passphrase-protected SSH setup, repository creation and push, post-commit auto-push hooks, and scheduled sync fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sgtbaixiao](https://clawhub.ai/user/sgtbaixiao)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding-agent users use this skill to configure GitHub authentication, repository creation, push workflows, and optional automatic push behavior from a Git Bash environment. It is especially oriented toward machines where network reachability determines whether HTTPS/GCM or SSH should be used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent auto-push behavior may automatically stage, commit, and push local repository contents without enough user control.

Mitigation: Enable auto-push only for reviewed repositories, verify secrets and private files are excluded before installation, and keep a removal plan for the post-commit hooks and scheduled task.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/SgtBaixiao/github-autosetup)
- [ClawHub skill page](https://clawhub.ai/sgtbaixiao/skills/github-autosetup)
- [Publisher profile](https://clawhub.ai/user/sgtbaixiao)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask the user to complete browser OAuth, SSH key passphrase entry, repository visibility confirmation, and other sensitive steps in their own terminal.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and plugin metadata; ClawHub release version 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
