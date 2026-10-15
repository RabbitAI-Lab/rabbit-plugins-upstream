## Description:

Helps agents generate 10–300-second music from text prompts through the dLazy-hosted ElevenLabs music service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request original background music, advertising music, and short-video soundtracks from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local inputs may be sent to dLazy, and generated files are hosted by dLazy.

Mitigation: Avoid sending sensitive material without approval and review the service terms before use.

Risk: Login can save an API key locally, and installing the third-party CLI can persist software on the host.

Mitigation: Use the on-demand npx option or dry-run when appropriate; protect and rotate API keys.

Risk: The documented sample response shows an image rather than music.

Mitigation: Check the actual result type and audio file before relying on the output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text commands and JSON service responses with hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download; asynchronous requests return a generation ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
