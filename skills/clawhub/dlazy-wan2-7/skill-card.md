## Description:

Tongyi Wanxiang 2.7 video model covers text-to-video, first/last-frame-to-video, and reference-to-video generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Wan 2.7 videos from text prompts, reference media, or first and last frames through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided media paths can be sent to dLazy's third-party cloud service.

Mitigation: Use the skill only for content appropriate to share with dLazy, and avoid passing sensitive prompts or media unless the user accepts that disclosure.

Risk: Authentication stores a dLazy API key locally or uses the DLAZY_API_KEY environment variable.

Mitigation: Protect the local config file and environment, rotate or revoke keys from the dLazy dashboard when needed, and prefer scoped credentials.

Risk: Global installation of the dLazy CLI increases local dependency persistence.

Mitigation: Use the pinned npx invocation when a user does not want to install the CLI globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of the dLazy CLI, which can return generated media URLs, output metadata, async task identifiers, or saved local assets.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
