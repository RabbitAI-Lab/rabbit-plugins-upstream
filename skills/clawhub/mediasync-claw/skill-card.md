## Description:

MediaSync-Claw lets an OpenClaw agent list, search, and return playback links for local media files through a Flask media service that can be exposed remotely through an FRP tunnel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yu-libin](https://clawhub.ai/user/yu-libin)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users use this skill to browse and play a local home media library from WhatsApp through AI-generated media links. It is intended for personal remote streaming on a Windows x64 host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make a local media service reachable from the public internet without built-in authentication.

Mitigation: Install only when public remote access is intended, review or add authentication before exposure, and do not rely on the public subdomain for privacy or access control.

Risk: Public access to the media service may expose local media files if the subdomain is discovered.

Mitigation: Run the skill on an isolated VM or dedicated host and place only non-sensitive MP4 files in the videos directory.

Risk: The release has a suspicious security verdict in the authoritative scan evidence.

Mitigation: Review the scan summary and guidance carefully before installation, especially when running on a primary workstation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yu-libin/skills/mediasync-claw)
- [MediaSync-Claw product documentation](https://poly-ai.chat/mediasync-claw)
- [FRP v0.65.0 release](https://github.com/fatedier/frp/releases/tag/v0.65.0)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [JSON responses containing text with media lists and playback links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces links for media files discovered in the local videos directory.]

## Skill Version(s):

0.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
