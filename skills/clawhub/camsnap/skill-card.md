## Description: <br>
Capture frames or clips from RTSP/ONVIF cameras. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use Camsnap to guide agents in configuring and running camera capture workflows for RTSP/ONVIF cameras, including discovery, snapshots, short clips, motion watches, and diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports access to camera endpoints, which may involve sensitive video feeds and credentials. <br>
Mitigation: Install and use it only when camera access is intended, keep camera passwords out of logs and shared chats, and use appropriate local credential handling. <br>
Risk: Motion watch actions can execute user-provided commands. <br>
Mitigation: Use watch actions only with commands that are fully understood and trusted, and review proposed commands before execution. <br>


## Reference(s): <br>
- [Camsnap homepage](https://camsnap.ai) <br>
- [Camsnap on ClawHub](https://clawhub.ai/steipete/skills/camsnap) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include camera names, capture durations, output file paths, motion thresholds, and trusted watch actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
