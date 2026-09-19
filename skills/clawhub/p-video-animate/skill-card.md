## Description:

Use when someone wants a photo to move like another video, including motion transfer, dance remixes, or performance variations from a template clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to animate a still image with motion transferred from a reference video through Pruna's p-video-animate model, while preserving the subject from the image and the motion from the template video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install mutable external skills with unpinned npx commands before use.

Mitigation: Review each install command, prefer pinned or reviewed versions where available, and avoid installing the full suite unless it is needed.

Risk: The workflow uploads user media to Pruna and uses a PRUNA_API_KEY for API calls.

Mitigation: Use only media appropriate for upload to Pruna, keep PRUNA_API_KEY scoped and private, and avoid exposing the key in logs or shared files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-animate)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY plus user-provided source video and reference image URLs; generated video duration follows the source video.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
