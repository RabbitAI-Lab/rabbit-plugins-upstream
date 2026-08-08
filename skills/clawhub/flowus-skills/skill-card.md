## Description: <br>
Use the FlowUs CLI safely for authorized API, content, and file tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flowus](https://clawhub.ai/user/flowus) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate the FlowUs CLI for authorized FlowUs API, page, database, search, Markdown, and file workflows while checking authentication and write intent before remote actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through installing or updating the FlowUs CLI distribution. <br>
Mitigation: Confirm trust in the FlowUs CLI distribution and require explicit user approval before install or update actions. <br>
Risk: FlowUs credentials may be exposed if copied into chat, command arguments, files, logs, or shared shells. <br>
Mitigation: Use saved credentials, FLOWUS_TOKEN, or an approved secret channel, and redact credentials from outputs. <br>
Risk: Authenticated FlowUs commands can create, update, append, upload, or replace workspace content. <br>
Mitigation: Verify authentication, target workspace, target object, operation, expected impact, and user approval before write actions. <br>


## Reference(s): <br>
- [FlowUs CLI ClawHub skill page](https://clawhub.ai/flowus/skills/flowus-skills) <br>
- [FlowUs CLI installer](https://cdn2.flowus.cn/flowus-cli/install) <br>
- [FlowUs CLI Windows installer](https://cdn2.flowus.cn/flowus-cli/install.ps1) <br>
- [FlowUs API base URL](https://api.flowus.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON command output guidance, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce FlowUs CLI commands, request body files, Markdown page content, and safety checks before authenticated or write actions.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
