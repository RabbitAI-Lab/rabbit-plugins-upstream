## Description:

Generates short videos quickly with Google Veo 3.1 Fast from text prompts or image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to create short text-to-video clips, guide a clip with first and last frame images, or extend a video through dLazy's hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and local media files may be uploaded for generation.

Mitigation: Avoid submitting sensitive prompts or media, and use only media you intend and are authorized to upload.

Risk: The skill requires trusting the external dLazy CLI and uses an API key stored in local CLI configuration.

Mitigation: Review the pinned @dlazy/cli version before installing, keep API keys out of chat, and rotate or revoke exposed keys.

## Reference(s):

- [dLazy CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Configuration guidance]

**Output Format:** [Generated video asset or URL with a JSON result envelope; command and setup guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short clips; frames mode supports 4, 6, or 8 seconds, and extend mode adds 7 seconds.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
