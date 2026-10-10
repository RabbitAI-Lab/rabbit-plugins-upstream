## Description:

Helps agents generate multilingual ElevenLabs text-to-speech with a choice of voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and other users can prepare voiceovers, audiobooks, and character dialogue from text using preset or custom voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speech prompts and any files supplied to the service are sent to dLazy's hosted API.

Mitigation: Send only content you are comfortable sharing with the third-party service.

Risk: Using the skill requires a dLazy API key and a pinned third-party CLI package.

Mitigation: Protect and rotate the API key, review the CLI before installing, and use the pinned on-demand package if a global install is unwanted.

Risk: The documented output sample shows an image rather than audio, and some error text refers to images or video.

Mitigation: Confirm actual audio output and error behavior instead of relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands; CLI responses provide JSON links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice selection and stability, similarity, and style controls; optional local download.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
