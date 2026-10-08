## Description:

Clones a voice from reference audio and generates spoken audio for new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate new speech from text using a voice they have permission to clone from reference audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference voice audio and local audio files may be sent to a hosted service.

Mitigation: Only submit audio you are comfortable sharing with dLazy; review local file paths before use.

Risk: Cloned speech can impersonate someone without consent.

Mitigation: Only clone voices you own or have explicit permission to use.

Risk: A saved API key can remain on the device after a session.

Mitigation: Use a per-invocation DLAZY_API_KEY when persistent credentials are undesirable, and rotate or revoke keys if exposed.

Risk: The documented response example shows an image instead of audio.

Mitigation: Check the actual output type and listen to generated audio before relying on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Audio links, Shell commands]

**Output Format:** [JSON response with hosted result URLs or an asynchronous task ID; CLI usage guidance in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirm that returned media is audio; the published example incorrectly shows an image.]

## Skill Version(s):

1.3.25 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
