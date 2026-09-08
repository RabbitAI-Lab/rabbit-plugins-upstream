## Description:

Fast version of ByteDance's Seedance 2.0 for faster video generation with multi-modal references, first/last frame inputs, and text-to-video prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through the dLazy Seedance 2.0 Fast CLI, including text-to-video generation and media-guided generation from image, video, audio, first-frame, or last-frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an external npm CLI with the user's account permissions.

Mitigation: Use the pinned npx invocation when possible, review the referenced CLI source before global installation, and install only in environments where running dLazy CLI is acceptable.

Risk: Prompts, parameters, and referenced local media files may be sent to dLazy cloud services for generation.

Mitigation: Only provide media and prompt content intended for upload to dLazy API and media storage endpoints.

Risk: The dLazy API key is a credential stored locally or supplied through the environment.

Mitigation: Store the key with user-only access, prefer scoped organization keys, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated media URLs, asynchronous task identifiers, or save generated assets to a local path.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
