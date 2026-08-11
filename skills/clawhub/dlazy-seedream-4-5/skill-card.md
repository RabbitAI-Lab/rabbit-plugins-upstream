## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images through the dLazy hosted Seedream 4.5 service from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected local reference images may be sent to the dLazy hosted service.

Mitigation: Avoid submitting confidential prompts or files unless the user has approved use of dLazy for that content.

Risk: Using the service may consume paid dLazy credits.

Mitigation: Confirm account credit usage expectations before running generation commands, especially for repeated or high-resolution requests.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use the documented login or auth command, keep the key scoped to the user account, and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned by the dLazy CLI as hosted file URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
