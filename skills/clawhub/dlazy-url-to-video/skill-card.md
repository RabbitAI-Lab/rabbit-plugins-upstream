## Description:

URL to Video helps an agent turn a supplied webpage URL into a promo, ad, or product demo video by using the dLazy hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and external users can use this skill when they have a URL and want an agent to generate a promotional, social ad, or product demonstration video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files may be sent to the third-party dLazy hosted service.

Mitigation: Only submit URLs, prompts, and files that are approved for use with dLazy, and avoid attaching sensitive or restricted data.

Risk: The skill uses a locally stored dLazy API key for hosted service access.

Mitigation: Store the key using the documented CLI authentication flow, restrict local config access, and rotate or revoke the key if exposure is suspected.

Risk: The workflow depends on a third-party npm CLI and network endpoints.

Mitigation: Review the pinned CLI package and source before installation, and confirm that access to api.dlazy.com and files.dlazy.com is acceptable in the deployment environment.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted service responses through the dLazy CLI and may reference project IDs for follow-up turns.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
