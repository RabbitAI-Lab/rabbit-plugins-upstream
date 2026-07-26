## Description: <br>
Controls an Android device running longarm through HTTP API or MCP tools for gestures, screenshots, app and intent launch, overlays, and batch automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[metaphorproj](https://clawhub.ai/user/metaphorproj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent operate a user-controlled Android device running longarm, including screen inspection, gestures, app or intent launch, and batch automation over HTTP or MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad remote control over an Android device, including screenshots, app launches, gestures, batch automation, and deletion commands. <br>
Mitigation: Install only when the user controls the Android device and trusts the longarm app and endpoint; review commands and batch tasks before running them. <br>
Risk: Screenshots and batch history may expose passwords, private messages, or other sensitive screen content. <br>
Mitigation: Avoid capturing sensitive screens and review screenshot or export destinations before saving or sharing outputs. <br>
Risk: The optional bearer token can grant remote-control access to the device endpoint. <br>
Mitigation: Protect LONGARM_TOKEN, use longarm on a trusted network, and avoid exposing the endpoint beyond intended users. <br>


## Reference(s): <br>
- [Longarm HTTP API Reference](references/api.md) <br>
- [Longarm MCP Reference](references/mcp.md) <br>
- [Server-resolved GitHub provenance](https://github.com/metaphorproj/longarm-skills/tree/main/skills/longarm-android-control) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, HTTP API calls, and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write screenshots or exported batch artifacts when the agent runs longarm commands.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
