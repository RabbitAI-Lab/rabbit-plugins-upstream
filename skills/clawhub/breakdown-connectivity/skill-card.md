## Description: <br>
Diagnose Internet, DNS, Wi-Fi, packet loss, latency, endpoint reachability, browser navigation, API, upload, download, MCP, and cloud-tool failures with Breakdown on macOS, including setup and discovery of the local MCP tools it provides. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peacecraft-circuit](https://clawhub.ai/user/peacecraft-circuit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users on macOS use this skill to add Breakdown network evidence to connectivity troubleshooting, readiness checks, and post-incident investigation. It can also guide installation and MCP client configuration when Breakdown is not yet available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation and MCP setup can change local applications and agent configuration. <br>
Mitigation: Review and approve installer launch, app opening, and Codex or Claude Code MCP configuration commands before running them. <br>
Risk: Connectivity evidence and analysis depend on a supported macOS environment, a running Breakdown app, and available MCP tools. <br>
Mitigation: Confirm macOS 13 or later, app and bridge availability, MCP discovery, and relevant tool availability before relying on reports or analysis. <br>


## Reference(s): <br>
- [Breakdown MCP tools](references/mcp-tools.md) <br>
- [Breakdown Mac download](https://breakdown.live/download/mac) <br>
- [Breakdown agent guide](https://breakdown.live/for-agents/) <br>
- [ClawHub skill page](https://clawhub.ai/peacecraft-circuit/skills/breakdown-connectivity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May refer to live Breakdown MCP tool results when the local app and bridge are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
