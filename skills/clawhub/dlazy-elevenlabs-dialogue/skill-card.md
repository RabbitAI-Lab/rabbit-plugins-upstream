## Description:

Creates multi-voice ElevenLabs dialogue audio from lines assigned to individual voices, with support for expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate voiced conversations for character scenes, podcasts, and short skits, assigning different voices to dialogue lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue prompts, parameters, and explicitly referenced files are sent to dLazy cloud services.

Mitigation: Only submit content you are authorized to share, and review any file inputs before calling the service.

Risk: Some written command and output examples appear to come from a different template.

Mitigation: Check `dlazy elevenlabs-dialogue -h` for actual options and verify the media type in the returned result.

Risk: Using this skill requires installing an external dLazy CLI.

Mitigation: Review the package before use; prefer the pinned `npx @dlazy/cli@1.2.3` invocation if a persistent global install is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio files]

**Output Format:** [CLI commands and JSON response containing generated media links; optional saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 10 distinct voices; asynchronous jobs can return a task ID instead of immediate media.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
