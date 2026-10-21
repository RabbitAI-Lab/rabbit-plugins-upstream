## Description:

Converts static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn reference images or first and last frames into short videos with Vidu Q2 through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are uploaded to dLazy, and generated media is hosted there.

Mitigation: Confirm the user wants to use the hosted service before sending sensitive or private media.

Risk: Authentication can store an API key in local CLI configuration.

Mitigation: Protect the local configuration or supply the key per invocation through the documented environment variable.

Risk: Broad image-to-video trigger wording can invoke the service unexpectedly.

Mitigation: Confirm intent before invoking it for generic image-to-video requests.

Risk: The skill depends on an external npm package.

Mitigation: Review the package and its listed source before installing in supply-chain-sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; the CLI can save results locally.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
