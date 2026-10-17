## Description:

Helps agents generate and edit images, videos, music, and other media through Sogni AI's GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill with an AI agent to generate, edit, and upscale images and video, create music and speech, and manage repeatable creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs a Sogni API key and can send selected prompts and media to Sogni services.

Mitigation: Use a dedicated API key and share only prompts or files approved for upload.

Risk: Media generation may incur charges, especially when cost confirmation is disabled.

Mitigation: Review estimated costs and avoid --no-confirm-cost unless the user expressly approves the spend.

Risk: Setup can register persistent integrations, and uninstall with --purge can remove saved credentials, memories, personas, and other local data.

Mitigation: Review persistent setup steps and uninstall without --purge when local Sogni data should be retained.

## Reference(s):

- [ClawHub release](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [Model catalog and sizing](references/models.md)
- [Hosted API and workflows](references/hosted-api.md)
- [Video prompting](references/video-prompting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Media files]

**Output Format:** [Markdown guidance and CLI commands; generated images, video, and audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hosted modes can upload selected local media to Sogni services.]

## Skill Version(s):

3.57.0 (source: ClawHub release metadata, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
