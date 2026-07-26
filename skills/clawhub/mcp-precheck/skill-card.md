## Description: <br>
Check MCP servers against the PolicyLayer registry before connecting to them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[policylayer](https://clawhub.ai/user/policylayer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to precheck MCP servers against PolicyLayer registry records before adding, connecting, or reviewing configured MCP servers. It guides stack scans, per-server checks, and optional hook installation while leaving connection decisions to the human operator. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the external PolicyLayer CLI and registry, so failed commands or network lookups mean a precheck did not run. <br>
Mitigation: Report command failures plainly, show the error, and avoid substituting memory or improvised analysis for a registry result. <br>
Risk: The optional hook changes Claude settings and affects future MCP additions. <br>
Mitigation: Install or remove the hook only after explicit human approval and confirm exactly what settings were written. <br>
Risk: Registry lookups may send MCP server identifier candidates such as package names, slug guesses, or config key names. <br>
Mitigation: Use package-only stack scans when config key names are sensitive and avoid sending config contents, environment values, or file paths. <br>


## Reference(s): <br>
- [MCP Precheck Skill Page](https://clawhub.ai/policylayer/skills/mcp-precheck) <br>
- [PolicyLayer Skill Source](https://policylayer.com/skill.md) <br>
- [PolicyLayer Dashboard](https://app.policylayer.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented reporting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose client-specific deny-rule configuration only after human approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
