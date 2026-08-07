## Description: <br>
gws CLI: Shared patterns for authentication, global flags, and output formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill as a shared reference for authenticating with the gws Google Workspace CLI, applying global flags, formatting output, and handling shell syntax safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The gws CLI can operate on Google Workspace data, including write or delete actions. <br>
Mitigation: Require user confirmation before write or delete operations and prefer dry-run validation where available. <br>
Risk: Google credentials, API keys, tokens, or sensitive Workspace content may be exposed through command output or logs. <br>
Mitigation: Do not print secrets directly, review credential scope separately, and use sanitization for PII or content safety screening when appropriate. <br>
Risk: Shell quoting mistakes can alter command arguments, especially zsh history expansion in sheet ranges or embedded JSON values. <br>
Mitigation: Use the documented quoting patterns for sheet ranges and JSON payloads before executing commands. <br>


## Reference(s): <br>
- [gws Google Workspace CLI repository](https://github.com/googleworkspace/cli) <br>
- [gws issue tracker](https://github.com/googleworkspace/cli/issues) <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/gws-shared) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance includes authentication patterns, global CLI flags, safety rules, and shell quoting examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
