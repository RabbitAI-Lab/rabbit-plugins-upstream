## Description: <br>
Provides core Git version-control command guidance for repository setup, commits, branching, remote synchronization, and history management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to ask an agent for Git command guidance and shell-command execution support for initialization, commits, branching, remotes, history inspection, undo workflows, stash usage, and basic collaboration tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad shell-based Git authority, including commands that can alter history, remotes, credentials, or untracked files. <br>
Mitigation: Before execution, require the agent to show git status, current branch, remote URL, and previews for cleanup commands; require explicit approval for push, pull --rebase, reset --hard, branch or tag deletion, credential changes, and git clean commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-essentials-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an agent with shell execution and Git 2.20+ available; commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
