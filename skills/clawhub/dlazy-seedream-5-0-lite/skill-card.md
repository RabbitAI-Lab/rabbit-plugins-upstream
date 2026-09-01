## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to have an agent generate or transform images through the dLazy Seedream 5.0 Lite CLI using prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dLazy API key may be stored on disk in the local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for per-run use when persistence is not needed, and verify permissions on ~/.dlazy/config.json if a key is saved.

Risk: Prompts and selected local images are sent to dLazy hosted services for generation.

Mitigation: Review prompts and input files before invocation, especially when they may contain sensitive or proprietary content.

Risk: Generation commands can incur paid API usage or overwrite intended output paths.

Mitigation: Use dry-run or explicit command options where appropriate, and provide clear output paths when saving generated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted file URLs and may be saved locally with the CLI --save option.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
