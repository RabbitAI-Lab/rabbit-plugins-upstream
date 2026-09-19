## Description:

A structured workflow skill dedicated to social-media carousel design using a single-confirmation, cover-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and design-focused agents use this skill to plan and generate social-media carousel image sets. It guides direction confirmation, cover-first generation, review, and matching slide production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media paths may be uploaded to dLazy cloud services during image generation.

Mitigation: Review data sensitivity before use and avoid submitting confidential prompts or media unless approved for the dLazy service.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for ephemeral use where appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The workflow depends on an external npm package and dLazy cloud endpoints.

Mitigation: Review the @dlazy/cli package or source before deployment and pin the reviewed CLI version in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tables, status updates, prompts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dLazy-hosted image result URLs after CLI execution.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
