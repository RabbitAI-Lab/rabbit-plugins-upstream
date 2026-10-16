## Description:

Guides agents in generating multi-voice dialogue audio with ElevenLabs eleven_v3 through dLazy, including per-line voice selection and expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce voiced conversations for character scenes, podcasts, and short skits, assigning voices to individual lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and selected local inputs are sent to dLazy's hosted service, and use requires a dLazy API key.

Mitigation: Confirm trust in dLazy and the pinned CLI package before installation; avoid submitting sensitive content without authorization and protect the API key.

Risk: The example command uses an undocumented --prompt flag, and the example output describes an image rather than dialogue audio.

Mitigation: Check the CLI help and supported options before invoking the skill; verify the actual output type rather than relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI homepage (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Audio]

**Output Format:** [Markdown guidance and CLI JSON response with a generated asset URL or optional saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 10 distinct voices per dialogue; asynchronous generation is available.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
