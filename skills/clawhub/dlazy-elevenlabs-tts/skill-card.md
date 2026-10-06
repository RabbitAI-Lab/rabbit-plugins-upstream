## Description:

Generates multilingual speech from text using ElevenLabs eleven_v3, with selectable voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate speech for dubbing, audiobooks, and character dialogue, choosing a voice and tuning its delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the dLazy npm CLI executes third-party software.

Mitigation: Review and trust the pinned package and service before installation or execution.

Risk: A dLazy API key may be saved to local CLI configuration.

Mitigation: Protect access to the configuration file and rotate or revoke the key if exposed.

Risk: Prompts and explicitly supplied files may be sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive content unless the service is approved for it.

Risk: The documented PNG result example appears inconsistent with text-to-speech output.

Mitigation: Check the actual command response and expect audio rather than relying on the example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a hosted audio result or an asynchronous task ID; it can also save the result locally.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release; bundled frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
