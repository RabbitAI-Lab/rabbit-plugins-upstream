## Description: <br>
Use when the user needs Xcode build/test/run workflows, simulator or device control, UI automation, screenshots/video, logs, or LLDB debugging through XcodeBuildMCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ipavlidakis](https://clawhub.ai/user/ipavlidakis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to drive repeatable Xcode build, run, test, simulator, device, UI automation, logging, media capture, and LLDB debugging workflows through XcodeBuildMCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an external XcodeBuildMCP package that may be installed with `latest`. <br>
Mitigation: Pin and review the external XcodeBuildMCP package before deployment. <br>
Risk: The skill can guide powerful Xcode automation actions involving devices, screenshots, logs, video, simulator cleanup, and LLDB commands. <br>
Mitigation: Use test simulators or devices when possible and require confirmation before media capture, log capture, physical-device installs, destructive simulator actions, or debugging commands. <br>


## Reference(s): <br>
- [XcodeBuildMCP Setup](references/mcp-setup.md) <br>
- [Xcodebuildmcp Workflows](references/workflows.md) <br>
- [ClawHub skill page](https://clawhub.ai/ipavlidakis/skills/xcodebuildmcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline MCP tool names and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include setup snippets, MCP tool recommendations, workflow steps, and verification guidance for screenshots, logs, or test results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
