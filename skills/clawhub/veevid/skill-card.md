## Description:

Guides agents in quoting and using the Veevid API to generate or edit video, images, and audio, transcribe speech, and run media tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meigesir](https://clawhub.ai/user/meigesir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can select Veevid media models, check credit costs, and generate or edit video, images, and audio through an agent. The skill also supports transcription, speech synthesis, and video processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded media or documents are sent to an external service and may contain sensitive information.

Mitigation: Review material before submission and upload only content the user is authorized to share.

Risk: Face, voice, and character-editing features could enable non-consensual or deceptive depictions of real people.

Mitigation: Require authorization and consent for real-person media, and decline deceptive or non-consensual edits.

Risk: Exposure of the locally stored API key could allow unauthorized use of the Veevid account.

Mitigation: Protect the key in ~/.config/veevid/api_key and do not share it in chat or generated output.

Risk: Media generation and draft upgrades consume credits, and understated input durations can cause extra charges.

Mitigation: Quote with accurate input details and obtain user approval before each paid request.

## Reference(s):

- [Veevid skill release](https://clawhub.ai/meigesir/skills/veevid)
- [Veevid API reference](artifact/references/api-reference.md)
- [Video models](artifact/references/models-video.md)
- [Image models](artifact/references/models-image.md)
- [Audio models](artifact/references/models-audio.md)
- [Video and image tools](artifact/references/models-tools.md)
- [Veevid API key setup](https://veevid.ai/settings/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API request examples and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes credit costs and requests confirmation before paid generation.]

## Skill Version(s):

1.3.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
