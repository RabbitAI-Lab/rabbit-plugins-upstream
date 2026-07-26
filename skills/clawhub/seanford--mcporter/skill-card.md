## Description: <br>
Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to operate MCP servers and tools from the command line, including listing servers, making tool calls, managing OAuth and configuration, running the daemon, and generating CLI or TypeScript interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MCP tool calls and server configuration changes can have side effects depending on the connected server. <br>
Mitigation: Review MCP server URLs, stdio commands, and configuration changes before running them, and use least-privilege accounts for OAuth. <br>
Risk: The skill guides use of a local CLI binary that must be present in the agent environment. <br>
Mitigation: Install only when mcporter is intended for use and confirm the required mcporter binary is available before following generated commands. <br>


## Reference(s): <br>
- [Mcporter homepage](http://mcporter.dev) <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/mcporter) <br>
- [Publisher profile](https://clawhub.ai/user/seanford) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend JSON output for machine-readable command results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
