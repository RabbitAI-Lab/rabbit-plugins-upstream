## Description:

Replicate an image or video reference by studying the provided media and recreating the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to recreate image or video references with their own subject, product, or characters through the dLazy hosted agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the dLazy hosted service.

Mitigation: Avoid attaching sensitive files unless the upload is intended and appropriate for the dLazy service.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use normal local credential protections and rotate or revoke the API key if needed.

Risk: Project history may persist across sessions.

Mitigation: Use the CLI session clearing option for sensitive projects when persistent context is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI GitHub page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands, authentication guidance, project continuation steps, and file attachment guidance.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
