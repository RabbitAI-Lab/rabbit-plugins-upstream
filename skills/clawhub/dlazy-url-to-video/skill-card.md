## Description:

Converts a supplied URL or webpage link into a promotional, ad, or product demo video workflow through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and content teams use this skill when a user provides a URL and wants the page transformed into a promo, social ad, or product demo video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to dLazy services.

Mitigation: Only use the skill with content approved for dLazy processing, and avoid attaching sensitive files unless the user has accepted that data transfer.

Risk: The skill depends on installing or invoking the third-party dLazy CLI from npm.

Mitigation: Review the dLazy CLI source and npm package before installation, and keep the CLI pinned to the version declared by the skill metadata.

Risk: The dLazy API key is required for execution and may be stored in local CLI configuration.

Mitigation: Use the authentication method the user is comfortable with, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The URL-to-video workflow is intended for requests that include a URL or link.

Mitigation: Confirm that the user supplied a URL or link before invoking the skill for generic video, ad, or product demo prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and selected attachments are sent to dLazy services.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
