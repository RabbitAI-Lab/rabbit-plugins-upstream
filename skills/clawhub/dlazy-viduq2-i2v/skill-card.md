## Description:

Helps agents turn still images into videos using Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating short videos from supplied images and prompts with the dLazy-hosted Vidu Q2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy cloud services.

Mitigation: Avoid sensitive media or prompts unless you are comfortable sharing them with the service.

Risk: The skill relies on an external npm CLI and a dLazy API key.

Mitigation: Review the pinned CLI package before installing and protect or rotate the API key as needed.

Risk: Some usage examples disagree with the documented CLI flags.

Mitigation: Check the installed CLI's help before running commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI repository (listed in skill metadata; not verified as skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The external service may return a generated media URL; the CLI can save the asset locally.]

## Skill Version(s):

1.3.24 (source: ClawHub release; included skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
