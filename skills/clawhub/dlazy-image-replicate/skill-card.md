## Description:

Analyzes a source image's visuals, composition, colors, lighting, and style, builds a replication prompt, and uses Seedream 4.5 through dLazy to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to ask dLazy's hosted image-replication service to generate a new image that follows the composition, colors, lighting, and style of one or more reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media files to the dLazy hosted API and media storage.

Mitigation: Only submit media you are comfortable uploading to dLazy, and review dLazy terms and data handling expectations before use in sensitive environments.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use a revocable API key, avoid exposing it in logs or shared shells, and rotate it if exposure is suspected.

Risk: The documented install path uses a pinned third-party CLI package.

Mitigation: Prefer the pinned npx invocation or an isolated shell for evaluation, and review the dLazy CLI source or package before global installation.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image URLs are returned from files.dlazy.com; async calls may return a generateId for polling.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
