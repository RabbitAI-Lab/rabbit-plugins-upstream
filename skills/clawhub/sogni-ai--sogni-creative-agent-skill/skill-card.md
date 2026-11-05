## Description:

Helps agents create and edit images, videos, music, and related media with Sogni AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use the skill to plan and run image, video, music, 3D asset, and media-editing workflows through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media generation may involve cloud processing, and hosted workflows upload referenced local files; this conflicts with advice in the skill about keeping private files on-device.

Mitigation: Do not provide files that must remain on-device; use only media approved for cloud processing.

Risk: Saved photos and voices may be reused in persona-based generations.

Mitigation: Get explicit approval before reusing saved photos or voices.

Risk: Asset publication may be immutable.

Mitigation: Confirm the destination and get explicit approval before publishing an asset.

Risk: External installers, dependency internals, and service-side data retention were not verified.

Mitigation: Use a reviewed package version and review relevant service terms before uploading sensitive media.

## Reference(s):

- [Sogni Creative Agent on ClawHub](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Model guide](references/models.md)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Hosted API guide](references/hosted-api.md)
- [Sogni pricing](https://docs.sogni.ai/pricing/#spark-packs)
- [npm package](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Generated image, video, audio, and 3D asset files, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected media task and model; media generation may incur charges.]

## Skill Version(s):

3.63.0 (source: CHANGELOG.md, released 2026-11-03)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
