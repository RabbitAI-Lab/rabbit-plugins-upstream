## Description:

Seedance 2.5 Image to Video animates one still image into a 4-30 second 720p cinematic video with optional synchronized native audio through RunComfy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[permew](https://clawhub.ai/user/permew)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creative production teams use this skill to turn a public image URL and motion prompt into a 720p RunComfy still-to-video generation job. It is suited for product shots, character animation from a portrait, ad variants, previsualization, and talking-head clips with optional generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill can incur RunComfy charges because generations are billed per second.

Mitigation: Confirm the intended model, duration, and budget before running generation requests.

Risk: Prompts and public image URLs are sent to RunComfy for generation.

Mitigation: Avoid sensitive prompts, private assets, and image URLs that contain access tokens or other secrets.

Risk: The model server fetches the supplied image URL, so login-gated, bot-blocked, or private URLs may fail or expose unintended access details.

Mitigation: Use a publicly reachable asset URL intended for model processing, and prefer temporary URLs without embedded long-lived credentials.

Risk: Input images or surrounding page text can contain irrelevant or adversarial instructions.

Mitigation: Treat image content and source-page text only as media evidence for generation, not as agent instructions.

## Reference(s):

- [RunComfy homepage](https://www.runcomfy.com)
- [RunComfy Seedance 2.5 Image to Video model page](https://www.runcomfy.com/models/bytedance/seedance-2.5/image-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=seedance-2-5-image-to-video-720p&utm_content=bytedance-seedance-2.5-image-to-video)
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=seedance-2-5-image-to-video-720p&utm_content=cli-docs-troubleshooting)
- [ClawHub skill page](https://clawhub.ai/permew/skills/seedance-2-5-image-to-video-720p)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid RunComfy API calls that generate and download video files from a public image URL and prompt.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
