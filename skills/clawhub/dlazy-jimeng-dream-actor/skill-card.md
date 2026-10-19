## Description:

Helps agents turn static character images into action videos using Jimeng Dream Actor through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to request action-video generation from a character image and motion prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy, and generated assets are hosted there.

Mitigation: Review media and prompts before submitting them to the hosted service.

Risk: API use may consume credits, and the skill requires a dLazy API key.

Mitigation: Check the cost estimate with dry-run where appropriate and review or rotate the API key as needed.

Risk: Installing the CLI globally leaves a persistent executable on the device.

Mitigation: Prefer the pinned on-demand npx invocation when a global installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns generated asset URLs or an asynchronous task ID; the CLI can save a result locally.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; bundled frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
