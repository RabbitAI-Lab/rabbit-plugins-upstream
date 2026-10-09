## Description:

Helps agents generate short sound effects from text descriptions for foley, ambience, alerts, and games using the dLazy ElevenLabs SFX service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short sound effects for video, games, and other audio projects through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly provided files are sent to dLazy's cloud service.

Mitigation: Send only content you are comfortable sharing with dLazy.

Risk: Using the service requires a dLazy API key.

Mitigation: Protect the key and rotate or revoke it when no longer needed.

Risk: Installing the third-party CLI requires trusting its npm package.

Mitigation: Review the pinned package before installing; use npx if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides users to generate and optionally save short sound effects; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; embedded skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
