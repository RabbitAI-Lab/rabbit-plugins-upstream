## Description:

Generates high-resolution 4MP raster images from prompts for print-ready and large-format creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate high-resolution raster artwork from text prompts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy; review the service terms before use.

Risk: Authentication may store an API key in local CLI configuration.

Mitigation: Protect the local key and rotate or revoke it through the dLazy dashboard if needed.

Risk: Running the CLI requires installing or executing a third-party package.

Mitigation: Review the package before use and prefer the pinned npx command if a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Images]

**Output Format:** [JSON response with image URLs; optionally a locally saved raster image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID to poll instead of an immediate image URL.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
