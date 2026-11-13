## Description:

Turns product footage into vertical ecommerce ads with FFmpeg, including hook-led edits, captions, calls to action, and platform-ready exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and ecommerce marketers use the skill to turn existing product, creator, or user-generated footage into short vertical ads for TikTok, Reels, and Meta. It guides hook-led recuts, pacing, captions, calls to action, audio levels, and export variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted FFmpeg fallback may send footage or media URLs to a third party.

Mitigation: Use local FFmpeg for sensitive footage, or assess the hosted service's handling of media before sending files or URLs.

Risk: The documented install commands use unpinned npm package versions, and the security scan leaves some references unresolved.

Mitigation: Review package sources and pin versions before installation; inspect unresolved referenced paths before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/ecommerce-video-edit)
- [Metadata homepage](https://github.com/vargHQ/skills/tree/main/ecommerce-video-edit)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video files, Image files]

**Output Format:** [Markdown instructions and shell commands; MP4 video exports and JPEG cover frames]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports can include a 9:16 ad, a 4:5 feed cut, and separate hook variants, depending on the footage and request.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
