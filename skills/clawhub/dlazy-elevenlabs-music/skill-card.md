## Description:

Generates 10–300-second original music from a natural-language prompt for background music, advertising, and short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request original music for background tracks, advertisements, and short-form video through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files explicitly provided to the CLI may be sent to the dLazy cloud service.

Mitigation: Avoid submitting sensitive content unless cloud processing is appropriate for it.

Risk: Login saves an API key in the user's local CLI configuration.

Mitigation: Protect the configuration file and rotate or revoke the key if exposed.

Risk: The documented image/png output example may not match generated music.

Mitigation: Check the actual returned asset type before using or distributing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (metadata link; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a generated asset link or asynchronous task ID; output media format should be checked.]

## Skill Version(s):

1.3.30 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
