## Description:

Generate and edit high-quality images with Nano Banana 2.0 through the dLazy CLI, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate with dLazy, call `dlazy banana2`, and generate or edit images from prompts and optional reference images through the hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local image files can be uploaded to dLazy cloud endpoints.

Mitigation: Use only inputs suitable for dLazy processing, and avoid passing sensitive local files unless the user accepts that upload.

Risk: `dlazy login` stores an API key in the local CLI configuration.

Mitigation: Use the npx form or per-run `DLAZY_API_KEY` when less local persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generic image-generation triggers could route broad image requests to dLazy unintentionally.

Mitigation: Confirm the user intends to use dLazy/Nano Banana before invoking the skill for generic image generation or editing requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON image-result payloads containing hosted output URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated images are returned as hosted files.dlazy.com URLs.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
