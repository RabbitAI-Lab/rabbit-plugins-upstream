## Description: <br>
ii-IRC helps agents maintain a persistent IRC presence through ii, monitor mentions, and send or read channel messages through file-based scripts and service guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[destructatron](https://clawhub.ai/user/destructatron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to set up an AI agent or bot on trusted IRC channels, monitor mentions through OpenClaw system events, and send or read IRC messages through ii file interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IRC mentions can pass raw channel text into the local OpenClaw agent without sender controls. <br>
Mitigation: Use only trusted or moderated channels; add sender and channel allowlists, event rate limits, message truncation or sanitization, and keep the agent's permissions limited. <br>
Risk: Watcher and service configuration can keep the bot reachable continuously. <br>
Mitigation: Disable the watcher or systemd services when the bot should not be reachable, and review generated service files before enabling them. <br>
Risk: IRC channel logs grow indefinitely and may expose more context than intended if read wholesale. <br>
Mitigation: Read bounded tails only and avoid ingesting the full ii out file. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/destructatron/skills/ii-irc) <br>
- [ii upstream site](https://tools.suckless.org/ii/) <br>
- [ii source repository](https://git.suckless.org/ii) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux and the ii binary; generated watchers should be used only in trusted or moderated channels.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
