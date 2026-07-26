## Description: <br>
Drive a native GUI app (macOS, Windows, Linux) via the cua-driver CLI or MCP server; snapshot its accessibility tree, click, type, or scroll by element index or pixel coordinates, and verify via re-snapshot without bringing the target to the foreground. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cua](https://clawhub.ai/user/cua) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and automation agents use this skill to operate real native desktop applications through Cua Driver while preserving a snapshot-action-verify loop and platform-specific permission boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants high-impact desktop automation authority, including screen inspection and input across native applications. <br>
Mitigation: Use it only for explicit GUI automation tasks, keep the window-scoped snapshot-action-verify loop, and require specific user intent before destructive actions. <br>
Risk: Installer examples execute remote shell or PowerShell scripts from the Cua Driver distribution endpoint. <br>
Mitigation: Prefer verified installers or trusted publisher installation paths, and run cua-driver doctor after installation before using automation capabilities. <br>
Risk: Browser attachment, screenshots, and session recordings may expose authenticated pages, full-screen contents, or typed actions. <br>
Mitigation: Prefer isolated browser profiles, require explicit approval before attaching to existing profiles or recording sessions, and treat trajectory and video outputs as sensitive. <br>
Risk: Embedded unrestricted mode can bypass Cua runtime approvals when a host application opts into that mode. <br>
Mitigation: Use standard embedded mode unless the host provides clear consent, logging, and permission UI, and keep unrestricted launch settings in trusted host configuration. <br>


## Reference(s): <br>
- [Cua Driver documentation](https://cua.ai/docs/cua-driver) <br>
- [Cua Driver ClawHub release](https://clawhub.ai/cua/skills/driver) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with CLI command examples and JSON tool arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include platform-specific setup steps, MCP or CLI invocations, and verification instructions for GUI automation workflows.] <br>

## Skill Version(s): <br>
0.11.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
