## Description: <br>
Install, connect, operate, and troubleshoot the host-neutral JS Eyes browser and Skill Runtime from CLI, MCP, or the optional OpenClaw adapter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imjszhang](https://clawhub.ai/user/imjszhang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install and diagnose JS Eyes, connect local browser automation through CLI, MCP, or OpenClaw, and manage the JS Eyes Skill Runtime. It is intended for local-first browser control workflows that require token-authenticated server, extension, and policy configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables an agent-controlled local browser runtime with access to browser operations and optional sensitive actions. <br>
Mitigation: Install only when that capability is intended, keep the server bound to localhost with token authentication, and review sensitive cookie, script, file upload, external-skill, and native-host changes before use. <br>
Risk: Installation or startup can change local browser integration through the optional Native Messaging host. <br>
Mitigation: Disable nativeHost.autoInstall unless token synchronization is required and confirm browser integration changes before enabling them. <br>
Risk: Risky install guidance can increase supply-chain exposure. <br>
Mitigation: Avoid curl-to-bash installation paths and prefer reviewed package installation and local configuration steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/imjszhang/skills/js-eyes) <br>
- [JS Eyes homepage](https://github.com/imjszhang/js-eyes) <br>
- [Security and Network Behavior](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces host setup, troubleshooting, security posture, and skill runtime operating guidance for local browser automation.] <br>

## Skill Version(s): <br>
2.10.0 (source: ClawHub release metadata; bundled frontmatter and package manifests report 2.9.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
