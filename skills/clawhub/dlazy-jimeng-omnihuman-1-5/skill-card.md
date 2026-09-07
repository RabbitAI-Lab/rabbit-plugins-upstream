## Description:

Generates realistic digital-human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to have an agent generate digital-human broadcast video assets from portrait imagery plus audio or text prompts through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and uploaded media to dLazy cloud endpoints for generation.

Mitigation: Only use prompts and media that are appropriate to upload to dLazy, and review the dLazy service and CLI links before use.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Treat the API key as a credential, run the CLI as an unprivileged user, and rotate or revoke the key if the machine or package is in doubt.

Risk: A global npm install persists the dLazy CLI binary on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or asynchronous task identifiers from the dLazy service.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
