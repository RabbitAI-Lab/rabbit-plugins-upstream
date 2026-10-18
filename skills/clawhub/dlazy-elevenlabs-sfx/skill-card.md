## Description:

Generates 1–22-second sound effects from text descriptions for foley, ambience, alerts, and games through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short sound effects for media, alerts, and games from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly provided to the hosted service may leave the local environment.

Mitigation: Avoid sending private prompts or media unless you intend to share them with dLazy.

Risk: Authentication stores a dLazy API key locally.

Mitigation: Protect the local account and rotate or revoke the key if it is exposed.

Risk: The skill uses an external npm CLI.

Mitigation: Review the pinned CLI package and its source before installation if supply-chain trust matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI returns a generated sound-effect URL or saves the asset locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release record)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
