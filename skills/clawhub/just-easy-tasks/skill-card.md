## Description: <br>
Use when an agent needs to work with Just Easy Tasks (JET) via the jet CLI or API: configure API key/context, find, create, update, complete, comment on, link, reference, or inspect tasks and project metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryan-w-s](https://clawhub.ai/user/ryan-w-s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use Jet to manage Just Easy Tasks workspaces and projects from an agent. It helps agents configure CLI context, inspect project metadata, and perform task operations such as finding, creating, updating, completing, commenting on, linking, and referencing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a JET API key and project or workspace context, which can expose or modify task-management data if over-scoped. <br>
Mitigation: Install only when the publisher and @just-easy-tasks/jet package are trusted, and provide an API key with only the access needed for the task. <br>
Risk: Destructive and administrative commands can change or delete shared workspace, project, membership, and task-management settings. <br>
Mitigation: Use --force or --dangerously-enable-admin-commands only when the user explicitly requests those actions and the target workspace or task is confirmed. <br>


## Reference(s): <br>
- [Just Easy Tasks](https://justeasytasks.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/ryan-w-s/skills/just-easy-tasks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-mode CLI command patterns for non-interactive agent use.] <br>

## Skill Version(s): <br>
1.0.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
