## Description: <br>
Wire Topical into OpenClaw with a hosted MCP server, inbound hook transform, and outbound webhook registration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daveangelcode](https://clawhub.ai/user/daveangelcode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to connect Topical end to end, including MCP access, local hook transform installation, and webhook registration guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup adds persistent OpenClaw MCP and hook configuration. <br>
Mitigation: Confirm the user intends to connect Topical to OpenClaw, merge configuration instead of overwriting unrelated keys, and verify the result with OpenClaw MCP and gateway checks. <br>
Risk: The workflow handles credentials including a Topical Agent API key, hooks token, and signing secret. <br>
Mitigation: Treat these values as secrets, avoid committing or logging them, keep hooks.token distinct from gateway.auth.token, and rotate exposed credentials. <br>
Risk: Hook transform modules run with gateway trust. <br>
Mitigation: Install transforms only from this artifact or the trusted companion @daveangelcode/topical skill before enabling the hook. <br>


## Reference(s): <br>
- [Topical](https://usetopical.com) <br>
- [Topical OpenClaw Setup on ClawHub](https://clawhub.ai/daveangelcode/skills/topical-openclaw-setup) <br>
- [Companion Topical Skill on ClawHub](https://clawhub.ai/daveangelcode/skills/topical) <br>
- [Topical OpenClaw Portal](https://app.usetopical.com/portal/openclaw/) <br>
- [Hosted Topical MCP Endpoint](https://app.usetopical.com/api/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local OpenClaw configuration changes and user-managed Topical portal registration.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
