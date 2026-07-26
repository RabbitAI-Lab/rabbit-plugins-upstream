## Description: <br>
Read and manage a signed-in Skylight Calendar family hub, including calendar events, chores, reward stars, shared lists, frames, and device information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and household administrators use this skill through an agent to inspect and update their own Skylight Calendar family hub data, including events, chores, reward stars, shared lists, frames, and devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawScan security summary reports an unpinned install path and broader live-account tool access than the submitted description discloses. <br>
Mitigation: Pin and review the npm package version before use, and only enable the server after reviewing the exposed Skylight tools. <br>
Risk: The skill requires Skylight account credentials and can change live family hub data. <br>
Mitigation: Use project-scoped configuration, set SKYLIGHT_FRAME_ID when possible, and require explicit user confirmation before deletes, bulk changes, uploads, member or account changes, and calendar changes. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp) <br>
- [Skylight](https://www.ourskylight.com) <br>
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples, shell commands, and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Skylight email and password environment variables; tool actions are scoped to a Skylight frame.] <br>

## Skill Version(s): <br>
0.4.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
