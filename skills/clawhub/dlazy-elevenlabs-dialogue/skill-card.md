## Description:

Helps agents generate multi-voice dialogue with ElevenLabs eleven_v3 through the dLazy service, assigning voices to individual lines and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce voiced conversations for character scenes, podcasts, and short skits with distinct speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text, parameters, and any media files supplied to the CLI may be sent to dLazy's hosted service.

Mitigation: Share only content authorized for external processing and review selected media paths before submission.

Risk: The CLI may store a dLazy API key in local configuration.

Mitigation: Protect the local credential or pass it for a single invocation through DLAZY_API_KEY; rotate or revoke a compromised key.

Risk: Documentation examples disagree with the dialogue options and depict an image result for an audio skill.

Mitigation: Check the installed command's help and inspect the actual response before relying on example flags or output types.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands; the CLI returns JSON containing result links or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dialogue accepts up to 20 lines and 10 distinct voices; generated assets can be saved locally.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
