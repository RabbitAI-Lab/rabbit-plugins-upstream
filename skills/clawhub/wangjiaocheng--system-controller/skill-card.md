## Description:

Controls Windows desktop software, system hardware, serial devices, IoT endpoints, and GUI automation through standalone command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable users use this skill to let an agent inspect and control a Windows workstation, connected serial devices, and smart-home endpoints. It is intended for workflows that require explicit confirmation before state-changing actions such as closing windows, killing processes, power operations, adapter changes, or device control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad control over desktop windows, processes, hardware settings, network adapters, serial devices, and smart-home APIs can affect the local system or connected devices.

Mitigation: Run the skill only in a dedicated, least-privileged environment and require explicit confirmation before state-changing actions.

Risk: Screenshots and OCR output may capture sensitive information from the active desktop.

Mitigation: Treat saved screenshots and OCR files as sensitive data, avoid using the skill around private content, and delete captured files when no longer needed.

Risk: Home Assistant and generic HTTP commands can expose long-lived tokens or send device commands over untrusted endpoints.

Mitigation: Avoid passing long-lived tokens on command lines or over HTTP; prefer short-lived credentials and trusted local endpoints.

Risk: The artifact can auto-install Python packages for serial, IoT, and GUI automation support.

Mitigation: Review dependency installation in a managed environment and approve required packages before operational use.

## Reference(s):

- [Windows System Controller - Command Reference](artifact/references/command_reference.md)
- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/system-controller)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or status-text command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target Windows 10/11 and may produce screenshots or OCR text when GUI automation is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
