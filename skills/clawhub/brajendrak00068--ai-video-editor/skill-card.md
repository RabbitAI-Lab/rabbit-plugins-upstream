## Description:

Edits videos with timeline trimming, captions, aspect-ratio reframing, audio and visual effects, and MP4 export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT

## Use Case:

Video creators and editors use this skill to turn source footage into short-form videos, podcast edits, and other finished clips with captions, reframing, audio work, and visual effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned package install, so the installed code may change between releases.

Mitigation: Review the package and pin a known version before installing and running it.

Risk: Prompts and media may be sent to a cloud service through public URLs.

Mitigation: Avoid sensitive footage unless the provider's data handling is understood; use only media URLs approved for cloud processing.

Risk: The security scan has partial coverage because some local references could not be resolved.

Mitigation: Review unresolved references and complete a full security scan before deployment.

## Reference(s):

- [Timeline Video Editor on ClawHub](https://clawhub.ai/brajendrak00068/skills/ai-video-editor)
- [Levea API key setup](https://www.livecore.ai/?openclaw=1)
- [Levea API endpoint](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [Video files, Text, JSON]

**Output Format:** [MP4 video export and structured tool responses (JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An edited MP4 is returned when export succeeds, with status and verification details.]

## Skill Version(s):

1.2.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
