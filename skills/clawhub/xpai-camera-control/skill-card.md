## Description:

Discovers and controls XPAI LAN cameras through MCP, including live viewing, snapshots, recording, PTZ, alarms, and device settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[catolin-zhang](https://clawhub.ai/user/catolin-zhang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and camera operators use this skill to discover and manage supported LAN cameras, view or record footage, adjust camera controls, and monitor events through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has access to camera administrator credentials and live camera footage.

Mitigation: Install only if you trust the publisher with camera access; limit camera permissions and rotate credentials exposed in chat or logs.

Risk: WebRTC previews or stream URLs could expose private live video beyond the intended audience.

Mitigation: Restrict browser previews to localhost or a trusted network, and share stream URLs only with authorized viewers.

Risk: Stored camera configuration, snapshots, recordings, and event data can expose sensitive information.

Mitigation: Restrict access to config.yaml, go2rtc.yaml, snapshots, recordings, and event files; retain them only as needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/catolin-zhang/skills/xpai-camera-control)
- [Supported devices](references/SUPPORTED_DEVICES.md)
- [Camera workflow](references/WORKFLOW.md)
- [Configuration reference](references/CONFIG.md)
- [MCP tools reference](references/MCP_TOOLS_API.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Images, Video]

**Output Format:** [Markdown responses, camera tool results, JPEG snapshots, and MP4 recordings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return live stream URLs and event records.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
