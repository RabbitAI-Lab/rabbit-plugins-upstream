## Description: <br>
Connects to a caller-configured Smartisan Notes service with a username or email and password to manage the current account's cloud workspace, query and edit notes, handle folders and note state, generate WeChat-ready rich HTML, and export Markdown or local Markdown files as themed PNG long images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaoolee](https://clawhub.ai/user/zhaoolee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to manage a self-hosted Smartisan Notes workspace through explicit service credentials, generate WeChat-ready HTML, and export Markdown notes as PNG long images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PNG export script executes .env files as shell code. <br>
Mitigation: Use only env files you created and inspected, keep them private, and avoid any .env file from an untrusted source. <br>
Risk: The skill can update, soft delete, permanently delete, or bulk export notes after authenticating to the configured service. <br>
Mitigation: Confirm destructive or bulk actions before running them, list or get real note IDs first, and use permanent deletion only when explicitly requested. <br>
Risk: Account credentials can be exposed if passed on the command line or committed in configuration files. <br>
Mitigation: Prefer private env files or environment variables, avoid echoing passwords, and do not commit NOTES_API_USERNAME or NOTES_API_PASSWORD values. <br>


## Reference(s): <br>
- [Workspace API and command reference](references/workspace-api.md) <br>
- [ClawHub skill release page](https://clawhub.ai/zhaoolee/skills/notes-export-api) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, HTML, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON/API outputs; scripts can write HTML and PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an explicit service base URL; note management also requires caller-provided account credentials.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
