## Description:

Remove an unwanted person, object, logo, or distraction from a video with Video Object Remover.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luffy2023100](https://clawhub.ai/user/luffy2023100)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this OpenClaw skill to remove one unwanted visual element from a video they own or are authorized to edit. The skill guides video upload, target selection, mask review, explicit erase confirmation, and final video retrieval through the Video Object Remover service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are uploaded to Video Object Remover for processing.

Mitigation: Use the skill only with videos the user owns or is authorized to edit, and review the mask preview before confirming the erase action.

Risk: The configured API key can spend account credits and access processed jobs.

Mitigation: Keep VIDEO_OBJECT_REMOVER_API_KEY private, avoid printing it or placing it in URLs, and do not retry failed create requests automatically.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luffy2023100/skills/video-object-remover-openclaw-skill)
- [Server-Resolved GitHub Source](https://github.com/luffy2023100/video-object-remover-openclaw-skill)
- [Video Object Remover Website](https://videoobjectremover.com)
- [OpenClaw Setup Guide](https://videoobjectremover.com/blog/remove-objects-from-video-with-openclaw)
- [Skill Instructions](https://videoobjectremover.com/skills/video-object-remover/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown guidance with inline shell commands, API status summaries, mask preview links, and completed video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires VIDEO_OBJECT_REMOVER_API_KEY and curl; accepts MP4, MOV, and WebM videos up to 100 MB.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
