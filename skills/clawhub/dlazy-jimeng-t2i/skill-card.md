## Description:

Guides an agent to generate images from text prompts using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text prompts and optional reference images into generated images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided local media are sent to dLazy's hosted services.

Mitigation: Send only content you are comfortable sharing with dLazy, and review local file inputs before invoking the skill.

Risk: The dLazy CLI requires an API key and can store it in a local configuration file.

Mitigation: Use a per-invocation DLAZY_API_KEY if persistent storage is unwanted; rotate or revoke credentials if exposed.

Risk: The skill relies on the external @dlazy/cli package.

Mitigation: Review the package and its source before installing; use the pinned npx invocation if a global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source (referenced by skill; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and JSON image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted remotely; the CLI can optionally download them to a local path.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
