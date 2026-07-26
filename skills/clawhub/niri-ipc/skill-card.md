## Description: <br>
Control the Niri Wayland compositor on Linux via its IPC (`niri msg --json` / $NIRI_SOCKET) to query session state and perform desktop actions from an OpenClaw agent running on a Niri session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atefr](https://clawhub.ai/user/atefr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Linux desktop users use this skill to let an agent inspect Niri compositor state, manage windows and workspaces, stream events, and invoke supported Niri IPC actions during an active Niri session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can manipulate the active Niri desktop session, including focusing, moving, and closing windows or reloading compositor configuration. <br>
Mitigation: Prefer read-only query commands by default and require explicit user approval before actions that change windows, workspaces, outputs, or compositor configuration. <br>
Risk: Raw IPC access and spawn actions can execute broad desktop or shell behavior outside strong safety boundaries. <br>
Mitigation: Use the higher-level helpers where possible, review raw IPC payloads before sending them, and require explicit approval before `spawn`, `spawn-sh`, direct socket requests, or event-stream automation. <br>


## Reference(s): <br>
- [Niri IPC quick reference](artifact/references/ipc.md) <br>
- [Upstream niri-ipc crate documentation](https://yalter.github.io/niri/niri_ipc/) <br>
- [ClawHub skill release page](https://clawhub.ai/atefr/skills/niri-ipc) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, Python helper scripts, and JSON IPC output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux, a running Niri session, the `niri` CLI, and `$NIRI_SOCKET` for direct socket access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
