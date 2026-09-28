## Description:

Helps agents generate vocal or instrumental music using inspiration or custom-lyrics modes through dLazy's Suno music service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request original music with automatically generated or supplied lyrics, with or without vocals, and retrieve the resulting media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files are sent to dLazy's hosted service, and generated results are hosted there.

Mitigation: Avoid sensitive prompts or media unless the service terms and data handling meet your needs.

Risk: Running the external CLI requires an API key that may be stored locally.

Mitigation: Review the CLI before installation, use the pinned npx invocation if a global install is undesirable, and protect or rotate the API key as needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON, Audio links]

**Output Format:** [Text instructions and CLI JSON responses containing hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID for later polling; generated assets can be saved locally.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
