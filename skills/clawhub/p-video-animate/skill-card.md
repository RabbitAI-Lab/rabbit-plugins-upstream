## Description:

Use when someone wants a photo to move like another video: motion transfer, dance remixes, or performance variations from a template clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to animate a still reference image with motion from a source video through Pruna's p-video-animate model. It helps agents collect required media inputs, prepare faithful motion-transfer prompts, and issue the documented Pruna API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video, image, and prompt details are sent to Pruna for remote processing.

Mitigation: Avoid uploading sensitive or regulated media, or images of people without permission.

Risk: The Pruna API key authorizes remote API calls if exposed.

Mitigation: Keep PRUNA_API_KEY private and avoid placing it in shared logs, prompts, or committed files.

## Reference(s):

- [p-video-animate ClawHub release page](https://clawhub.ai/pruna-ai/skills/p-video-animate)
- [Pruna files API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with inline bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-supplied image and video assets; remote output duration follows the source video.]

## Skill Version(s):

1.0.10 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
