## Description:

Generates videos from multiple reference images and prompts through LinkFox, supporting KLING, SEED, SEED_FAST, and HAPPY_HORSE with controls for duration, Pro mode, sound, aspect ratio, and resolution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos from multiple image URLs and a prompt through LinkFox AIGC models. It is useful when an agent needs to create multi-reference video outputs while controlling model, duration, resolution, aspect ratio, sound, and quality options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, and generation parameters are sent to LinkFox using the user's LinkFox API key.

Mitigation: Avoid submitting confidential prompts or sensitive image URLs unless that sharing is appropriate for the user's data policy.

Risk: Generated media and raw response data may be saved in local session media and data directories.

Mitigation: Review where session files are stored and share only the saved local output paths that are intended for the user.

Risk: Optional feedback submission can send user-provided comments to a LinkFox feedback endpoint.

Mitigation: Do not include confidential information in feedback content.

## Reference(s):

- [Multi-reference video API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen-multi)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [Plain text status and saved local media paths; generated videos are stored as local media files, with JSON response data saved locally when no video file is produced.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous generation can take several minutes and polling times out after 20 minutes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
