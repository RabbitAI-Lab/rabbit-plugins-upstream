## Description:

Generates 1MP raster images from text prompts for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use the skill to generate raster images from prompts and select an aspect ratio for quick creative iterations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided media are sent to dLazy's hosted service.

Mitigation: Review the CLI and service terms before submitting sensitive prompts or files.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when local key persistence is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI repository (declared CLI link, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image files]

**Output Format:** [CLI guidance and JSON results with hosted image URLs; optional saved raster image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratio selection, dry runs, asynchronous jobs, and local download.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
