## Description:

Generate/edit high-quality images with Nano Banana 2.0, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images through the dLazy Nano Banana 2 cloud service using prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and selected local media may be sent or uploaded to dLazy cloud endpoints.

Mitigation: Use the skill only with data approved for dLazy processing and avoid submitting sensitive local media unless the user accepts that transfer.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-run environment keys where appropriate, and rotate or revoke stored keys from the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns image output metadata, including hosted result URLs, and can save generated assets to a local path when requested.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
