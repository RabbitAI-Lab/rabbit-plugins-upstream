## Description: <br>
AI-powered image and video generation. Generate images, videos, manage jobs, and explore models via the masonry CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[junaid1460](https://clawhub.ai/user/junaid1460) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate images or videos from prompts, discover available Masonry models, monitor generation jobs, and download completed media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Masonry token could be exposed if pasted into chat or stored insecurely. <br>
Mitigation: Set MASONRY_TOKEN through a secret manager or environment variable, and avoid sharing tokens in conversation. <br>
Risk: Private prompts or reference images may be processed by Masonry's external generation service. <br>
Mitigation: Review prompt and image sensitivity before submission, and avoid sending private content unless the user accepts that processing. <br>
Risk: Generation jobs may consume subscription credits. <br>
Mitigation: Confirm user intent before starting jobs that may spend credits. <br>
Risk: Fabricated model keys or job IDs can mislead users or cause failed operations. <br>
Mitigation: Use only model keys, job IDs, and status values returned by Masonry CLI output. <br>


## Reference(s): <br>
- [Masonry homepage](https://masonry.so) <br>
- [Masonry pricing](https://masonry.so/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/junaid1460/skills/masonry-generate-image-and-video) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Masonry CLI commands and JSON response handling notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the masonry CLI and MASONRY_TOKEN; generation jobs may download media files and emit MEDIA file paths.] <br>

## Skill Version(s): <br>
1.1.6 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
