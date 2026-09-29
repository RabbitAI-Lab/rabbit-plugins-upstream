## Description:

Generates multilingual speech with ElevenLabs eleven_v3 using curated voices and adjustable voice settings through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate speech for dubbing, audiobooks, and character dialogue, with voice and delivery controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party CLI executes software locally.

Mitigation: Review the pinned @dlazy/cli package and its source before installing or running it.

Risk: Login stores an API key locally, and prompts are sent to dLazy's hosted API.

Mitigation: Protect the local key and avoid submitting sensitive text unless the hosted service is approved for it.

Risk: Generation may consume paid credits, and the example result describes an image instead of audio.

Mitigation: Check the cost estimate before generation and verify the returned asset type rather than relying on the sample output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and descriptions of JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated speech is returned through the hosted service; the bundled JSON example shows an image rather than audio and should be checked against actual results.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
