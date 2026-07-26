## Description: <br>
Claw Desktop Pet provides guidance for installing and operating a Windows desktop AI assistant with fault tolerance, auto-restart, performance monitoring, voice output, logging, and resource cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kk43994](https://clawhub.ai/user/kk43994) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to set up and configure a 24/7 desktop assistant with voice notifications, health monitoring, logs, and recovery behavior on Windows 10 or 11. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The desktop assistant installs and runs local Node.js and Python dependencies. <br>
Mitigation: Review the referenced repository and dependency manifests before installation, and avoid running the application with administrator privileges. <br>
Risk: The assistant exposes an OpenClaw bridge and is intended for always-on operation with logging and auto-restart behavior. <br>
Mitigation: Keep the bridge bound to localhost, confirm how to stop the app or disable auto-restart, and review cache and log cleanup settings before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kk43994/skills/claw-desktop-pet) <br>
- [Project README](https://github.com/kk43994/claw-desktop-pet#readme) <br>
- [Technical Documentation](https://github.com/kk43994/claw-desktop-pet/tree/master/docs) <br>
- [Release Notes v1.3.0](https://github.com/kk43994/claw-desktop-pet/blob/master/RELEASE-v1.3.0.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include install steps, configuration values, local service checks, log inspection commands, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and artifact CHANGELOG dated 2026-02-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
