## Description: <br>
Do Cli helps agents and terminal users install and operate the `do` command-line client for todo and life-tracking workflows through the do REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbeverhelst](https://clawhub.ai/user/robbeverhelst) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and users of the do personal productivity app use this skill to configure scoped API-key access and run daily task and habit workflows from a terminal or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents the CLI as agent-safe while the commands can capture tasks, mark tasks done, snooze tasks, and log habits in a real personal account. <br>
Mitigation: Install only for the intended do account, use a narrowly scoped API key, and require explicit user intent before commands that change task or habit data. <br>
Risk: Saved configuration can expose broad account access to later agent runs if a key has more scope than the workflow needs. <br>
Mitigation: Prefer environment variables for agent and CI runs, avoid persisting unnecessary credentials, and grant only the scopes required for the requested workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robbeverhelst/do-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and JSON-oriented CLI output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The described commands may read or change personal task and habit data depending on the scoped API key and command invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
