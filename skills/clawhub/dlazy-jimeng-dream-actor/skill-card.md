## Description:

Turns a static character image into an action video using Jimeng Dream Actor through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a character image and text prompt into a generated action video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media and prompts may be sent to dLazy's cloud service.

Mitigation: Confirm media paths and content before invoking the skill; use the service only if its data handling is acceptable.

Risk: Generation may consume paid API credits.

Mitigation: Check the cost estimate with dry-run and confirm available credits before generating.

Risk: A saved API key persists in local configuration.

Mitigation: Prefer a per-run API key or review the local credential configuration before saving a key.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Asset links]

**Output Format:** [Markdown with commands and generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a task ID for asynchronous requests; output files can be downloaded locally.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
