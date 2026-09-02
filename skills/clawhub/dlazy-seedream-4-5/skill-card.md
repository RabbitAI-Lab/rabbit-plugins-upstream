## Description:

Generate high-quality images with Doubao Seedream 4.5, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images through the dLazy CLI-backed Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local image inputs may be sent to dLazy-hosted services, with outputs hosted on files.dlazy.com.

Mitigation: Avoid private images and sensitive prompts unless that external processing is acceptable for the intended use.

Risk: The dLazy API key may be stored locally and can authorize usage or charges for the user's organization.

Mitigation: Protect the local CLI configuration, prefer scoped credentials where available, and rotate or revoke keys when access changes.

Risk: Broad image-generation triggers could route ordinary image requests to an external paid provider.

Mitigation: Install and invoke the skill only when dLazy and Seedream are the intended image provider for the workflow.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes containing generated image URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated image assets locally with --save; asynchronous mode returns a generateId for later polling.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
