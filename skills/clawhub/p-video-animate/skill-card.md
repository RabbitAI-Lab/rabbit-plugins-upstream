## Description:

Use when someone wants a photo to move like another video: motion transfer, dance remixes, or performance variations from a template clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to animate a still image with motion from a source video through Pruna's hosted video-animation service. The agent gathers the source video, reference image, resolution, frame rate, and any narrow instruction prompt before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected images, videos, prompts, and the Pruna API key to Pruna's hosted service.

Mitigation: Use only media and prompts approved for third-party processing, and handle PRUNA_API_KEY as a secret.

Risk: Using disable_safety_checker can change the safety and policy behavior of a generation request.

Mitigation: Avoid disable_safety_checker unless the user has an approved reason and understands the safety impact.

Risk: A reference image that does not match the template video's opening pose or framing can reduce motion-transfer fidelity.

Mitigation: Run the documented fidelity check before paid generation and adjust the reference image with the appropriate image-editing skill when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-animate)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY plus image and video inputs; generated video duration follows the source video.]

## Skill Version(s):

1.0.11 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
