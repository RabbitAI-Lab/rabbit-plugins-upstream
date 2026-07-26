## Description: <br>
Add a native Olvid channel in OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmartel-olvid](https://clawhub.ai/user/jmartel-olvid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and developers use this skill to connect an agent to Olvid for direct or group messaging with authenticated end-to-end encryption. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles private Olvid messages and a client key that may be stored in OpenClaw configuration. <br>
Mitigation: Install only after review, keep the client key secret, and prefer a protected configuration or environment-based secret handling where available. <br>
Risk: The release pins a reportedly vulnerable OpenClaw host version. <br>
Mitigation: Use the skill only on a patched OpenClaw host and recheck compatibility before deployment. <br>
Risk: Incoming attachments are written under /tmp/olvid-attachments. <br>
Mitigation: Restrict host access to the attachment directory and clear stored attachments according to local retention policy. <br>
Risk: The skill connects to a configured Olvid daemon target. <br>
Mitigation: Verify the daemon URL before use and limit it to the intended trusted daemon. <br>


## Reference(s): <br>
- [Olvid Channel on ClawHub](https://clawhub.ai/jmartel-olvid/skills/olvid-channel) <br>
- [Olvid OpenClaw documentation](https://doc.bot.olvid.io/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Olvid channel messages and OpenClaw configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports direct and group chats, replies, reactions, and media attachments through a configured Olvid daemon.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
