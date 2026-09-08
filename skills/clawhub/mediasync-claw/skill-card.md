## Description:

MediaSync-Claw helps an OpenClaw agent list, search, and stream local MP4 files through WhatsApp using a local Flask media server, FRP tunneling, and WebRTC signaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yu-libin](https://clawhub.ai/user/yu-libin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and OpenClaw developers use this skill to make a local personal media folder searchable from an OpenClaw-connected WhatsApp channel and return playback links for matching MP4 files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a local media server to the public internet without authentication.

Mitigation: Install only when public remote media access is intended, run it in an isolated VM or spare machine, and avoid placing sensitive media in the videos folder.

Risk: The skill downloads and executes a third-party FRP tunneling binary.

Mitigation: Do not whitelist or run frpc.exe unless you accept the supply-chain risk, and keep execution isolated from primary workstations and sensitive data.

Risk: Anyone who discovers the yunfrp.net subdomain may try to list or fetch media.

Mitigation: Assume the generated public endpoint can be discovered and stop the skill or tunnel when remote streaming is not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yu-libin/skills/mediasync-claw)
- [MediaSync-Claw README](artifact/README.md)
- [MediaSync-Claw Product Page](https://poly-ai.chat/mediasync-claw)
- [FRP v0.65.0 Release](https://github.com/fatedier/frp/releases/tag/v0.65.0)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON responses containing human-readable media lists and playback links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public playback URLs for discovered local MP4 files.]

## Skill Version(s):

0.1.10 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
