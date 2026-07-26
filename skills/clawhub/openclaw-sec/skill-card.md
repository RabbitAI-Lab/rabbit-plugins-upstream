## Description: <br>
AI Agent Security Suite - Real-time protection against prompt injection, command injection, SSRF, path traversal, secrets exposure, and content policy violations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paolorollo](https://clawhub.ai/user/paolorollo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security engineers use this skill to validate AI agent prompts, tool calls, shell commands, URLs, paths, and content for common agent security threats before execution or logging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install hooks that inspect agent prompts and tool calls. <br>
Mitigation: Review the installed hook files and enable them only in intended workspaces before relying on automatic protection. <br>
Risk: Security events, prompts, tool-call data, and findings may be retained in local logs or databases. <br>
Mitigation: Set retention periods deliberately, review stored data access, and vacuum or purge databases according to local policy. <br>
Risk: Owner bypass lists and fail-open hook behavior can reduce protection coverage. <br>
Mitigation: Keep owner bypass lists narrow, test hooks after installation, and monitor hook logs for execution errors. <br>
Risk: Notification webhook settings may send security event data to external systems. <br>
Mitigation: Configure only trusted webhook endpoints and review notification payloads before enabling integrations. <br>
Risk: A custom OPENCLAW_HOOKS_DIR value can change where hooks are installed. <br>
Mitigation: Use a trusted hooks directory and avoid running installation with an untrusted OPENCLAW_HOOKS_DIR value. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paolorollo/skills/openclaw-sec) <br>
- [README.md](README.md) <br>
- [Hooks guide](hooks/README.md) <br>
- [Example configuration](config.example.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and terminal-style text with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Security validation results may include severity, action, findings, recommendations, event history, statistics, and configuration guidance.] <br>

## Skill Version(s): <br>
0.2.6 (source: server release metadata; artifact frontmatter lists 1.0.2 and package.json lists 0.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
