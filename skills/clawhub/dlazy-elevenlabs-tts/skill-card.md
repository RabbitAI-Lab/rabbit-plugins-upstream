## Description:

Generates ElevenLabs eleven_v3 speech from text with multilingual voice selection and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text into multilingual speech for dubbing, audiobooks, and character dialogue, choosing a voice and adjusting speech style controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a CLI login operation whose purpose is not clear from the text-to-speech description, and the CLI package could not be fully resolved during scanning.

Mitigation: Review the CLI package and its login behavior before installing or authenticating; use credentials only with a service and publisher you trust.

Risk: The skill documentation says prompts and parameters are sent to a hosted service for generation.

Mitigation: Avoid submitting sensitive text unless you are comfortable sending it to the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [CLI project homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage (linked in skill documentation)](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset with a JSON result envelope containing asset information; the asset can also be saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice selection and stability, similarity, and style controls; asynchronous generation can return a task identifier.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
