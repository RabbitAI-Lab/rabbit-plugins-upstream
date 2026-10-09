## Description:

Helps agents request 10–300-second original music from a text prompt using ElevenLabs music_v1 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate music for backgrounds, advertisements, and short videos from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party npm CLI introduces supply-chain exposure.

Mitigation: Review the CLI source and package before installation; use the pinned npx invocation to avoid a persistent global install.

Risk: Prompts and any local input files explicitly provided may be sent to dLazy's hosted services.

Mitigation: Avoid supplying sensitive prompts or files unless their transfer to the service is acceptable.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect local credentials and use the per-invocation environment variable when persistent storage is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a hosted result URL or an asynchronous task ID; an optional flag downloads the result.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
