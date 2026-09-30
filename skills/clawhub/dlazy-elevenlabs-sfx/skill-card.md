## Description:

Guides an agent to generate 1–22-second sound effects from text descriptions using the dLazy ElevenLabs SFX CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short foley, ambience, alert, and game sound effects from a text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party npm CLI requires trusting its code and handling a dLazy API key.

Mitigation: Review the pinned CLI package before installation and keep the API key private.

Risk: Prompts and any media files supplied to the CLI may be sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive prompts or files and confirm cloud processing is acceptable.

Risk: Generation can consume paid credits.

Mitigation: Use the CLI's dry-run cost estimate before requesting generation.

Risk: The documented sample response incorrectly identifies the sound asset as an image.

Mitigation: Treat the generated asset as audio and inspect the actual response before processing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service generates audio assets; the skill's sample response mistakenly shows an image.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
