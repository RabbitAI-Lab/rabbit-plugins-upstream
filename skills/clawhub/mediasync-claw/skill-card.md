## Description:

MediaSync-Claw lets an OpenClaw agent list and share local MP4 files through a Flask media service exposed over a public FRP tunnel for remote playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yu-libin](https://clawhub.ai/user/yu-libin)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users use this skill to let an agent enumerate local MP4 files and return remote playback links through a connected chat channel. It is intended for personal media sharing, with the important caveat that the local service is exposed through a public third-party tunnel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically exposes a local unauthenticated media service through a public third-party tunnel.

Mitigation: Run it only when public sharing is intended, use a dedicated machine or VM, and store only non-sensitive MP4 files in the videos directory.

Risk: Anyone who discovers the public subdomain may be able to access the exposed media service.

Mitigation: Prefer a version that adds authentication, explicit tunnel opt-in, and a way to disable public exposure by default.

Risk: The skill downloads and executes a third-party FRP binary.

Mitigation: Use versions that verify pre-existing binaries and pinned dependencies, and review checksum updates before upgrading the FRP binary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yu-libin/skills/mediasync-claw)
- [Publisher profile](https://clawhub.ai/user/yu-libin)
- [FRP v0.65.0 release](https://github.com/fatedier/frp/releases/tag/v0.65.0)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [JSON response containing human-readable text with media file names and playback links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent action accepts an optional query object and returns a single text field for conversational rendering.]

## Skill Version(s):

0.1.8 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
