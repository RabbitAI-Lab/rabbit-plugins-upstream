## Description:

Upload an image or video to PostLake and attach it to a post. Use when a post needs media, or for platforms that require it (Instagram, TikTok, YouTube, Pinterest).

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to upload images or videos to PostLake, receive a media id, and attach the media to publish or schedule requests for social platforms that require media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill can upload chosen local or downloaded media to PostLake and create posts through accounts accessible to the provided API key.

Mitigation: Confirm the selected file, account targets, and API key scope before running upload or post creation commands.

Risk: Incorrect content type or oversized media can cause upload failure.

Mitigation: Set the real Content-Type and keep images at or below 20MB and videos at or below 200MB.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/postlake/skills/postlake-media)
- [PostLake API base URL](https://api.postlake.dev)
- [PostLake media upload endpoint](https://api.postlake.dev/v1/media)
- [PostLake posts endpoint](https://api.postlake.dev/v1/posts)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTLAKE_API_KEY; upload requests send selected media bytes to PostLake.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
