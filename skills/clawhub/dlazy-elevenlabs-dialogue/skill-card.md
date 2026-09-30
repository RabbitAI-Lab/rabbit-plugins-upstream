## Description:

Generates multi-voice dialogue audio with ElevenLabs eleven_v3, assigning voices to individual lines and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare character dialogue, podcasts, and short-form scenes with distinct voices and expressive delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI stores or reads a dLazy API key.

Mitigation: Protect the key, avoid sharing it in prompts or logs, and rotate or revoke it if exposed.

Risk: Prompts and explicitly supplied local media may be sent to dLazy's hosted service.

Mitigation: Check content and media for sensitive information before sending them.

Risk: The documented --inputs example and sample image response do not reliably describe dialogue audio output.

Mitigation: Consult the installed CLI help and confirm the response format before automating calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI requests dialogue audio from a hosted service; the documented response example may not reflect the actual audio format.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
