## Description:

Generates 10–300 seconds of original music from a natural-language prompt using ElevenLabs music_v1 for background music, ads, and short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to generate music for background tracks, advertisements, and short-form videos from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied local media may be sent to dLazy's cloud service.

Mitigation: Do not submit sensitive material without authorization; review the data being sent before generating.

Risk: Installing the CLI or saving an API key creates a local software and credential footprint.

Mitigation: Review the pinned @dlazy/cli package before installation; use npx and a per-invocation DLAZY_API_KEY when a global install or saved key is not wanted.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a JSON result with a hosted output URL or an asynchronous task ID; the --save option downloads the generated asset.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
