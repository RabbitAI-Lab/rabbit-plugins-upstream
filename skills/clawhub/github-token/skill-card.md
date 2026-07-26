## Description: <br>
Interact with GitHub using Personal Access Tokens for cloning repositories, managing branches, pushing changes, opening pull requests, creating issues, and viewing repository information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannyshmueli](https://clawhub.ai/user/dannyshmueli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to perform GitHub repository tasks with a user-provided Personal Access Token instead of OAuth. It is suited for controlled cloning, branch management, pull requests, issues, and repository inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A GitHub Personal Access Token can grant powerful repository access and may be exposed if stored in shared files, command-line history, logs, or authenticated clone URLs. <br>
Mitigation: Use a fine-grained, short-lived token limited to the needed repository and scopes; prefer environment-based handling, avoid storing the token in TOOLS.md or command lines, and revoke it when finished. <br>
Risk: The push workflow can stage and push all local changes, including unintended files. <br>
Mitigation: Review git status and diffs before pushing, use a dedicated branch, and commit only intended changes. <br>


## Reference(s): <br>
- [GitHub Personal Access Tokens](https://github.com/settings/tokens) <br>
- [GitHub REST API](https://api.github.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/dannyshmueli/skills/github-token) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and Python CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a user-provided GitHub token via environment variable or command option.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
