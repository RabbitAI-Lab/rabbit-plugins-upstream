## Description: <br>
Secure Script Runner is a documentation skill for storing encrypted scripts in MGC Blackbox and guiding explicit, user-approved local execution through MCP, REST API, or WebUI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and AI-agent users use this skill to document workflows for encrypted local script storage, explicit script execution, credential access review, and script sealing with MGC Blackbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local script execution can run untrusted or harmful code on the user's machine. <br>
Mitigation: Require explicit user authorization and review the script source, purpose, sensitive-data access, and dangerous-command risk before execution. <br>
Risk: Scripts may access local MGC credentials or sensitive outputs. <br>
Mitigation: Confirm token access, expected outputs, and credential need before allowing mgc_get with action="run" or any credential calls. <br>
Risk: Zero-exposure execution means the agent may not be able to inspect plaintext script content before running it. <br>
Mitigation: Only run scripts from trusted sources after a human verifies the script provider and purpose. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/secure-script-runner) <br>
- [MGC Blackbox project](https://github.com/zkeviny/MGC-Blackbox) <br>
- [MGC Blackbox issues](https://github.com/zkeviny/MGC-Blackbox/issues) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline Python, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; local script execution requires explicit user authorization.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
