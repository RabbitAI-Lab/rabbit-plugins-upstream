## Description:

This tool automatically downloads and executes the third-party 'frpc' binary from GitHub to establish an active outbound reverse tunnel. It exposes local file systems and port 8000 to the public internet via yunfrp.net subdomains. Additionally, it initiates outbound WebSocket/WebRTC signaling and connects to external STUN servers for peer-to-peer media streaming, enabling remote file access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yu-libin](https://clawhub.ai/user/yu-libin)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users use this skill to list, search, and stream media files from a local videos folder through WhatsApp-triggered agent actions and generated player links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically exposes local videos through a public unauthenticated tunnel.

Mitigation: Install only when public remote media access is intentional, keep only non-sensitive MP4 files in the videos folder, and review the artifact before normal use.

Risk: The public hostname and MD5 checksum do not provide access control.

Mitigation: Do not treat generated links as secrets or authorization; run the skill in a VM, dedicated device, or low-privilege account.

Risk: Plaintext public routing and automatic tunnel startup expand host exposure.

Mitigation: Isolate the runtime environment and stop or disable the skill when remote access is not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yu-libin/skills/mediasync-claw)
- [MediaSync-Claw Product Documentation](https://poly-ai.chat/mediasync-claw)
- [FRP v0.65.0 Release](https://github.com/fatedier/frp/releases/tag/v0.65.0)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration]

**Output Format:** [JSON API responses containing Markdown-style media lists and generated playback links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated links route playback through the configured public hostname and AIpollo player URL.]

## Skill Version(s):

0.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
