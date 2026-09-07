## Description:

Creates marketing, promotional, advertising, and brand videos from a product, brand, or brief for social media or campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to drive dLazy's hosted video agent for conversion-focused ecommerce, product, brand, and campaign videos. It supports product specifications, manuals, catalogs, or marketplace listings as inputs and can include multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service and uploaded files may be stored by dLazy media storage.

Mitigation: Avoid uploading secrets, confidential unreleased assets, or regulated data unless the organization accepts dLazy's service and retention model.

Risk: The CLI stores an API key locally and can also receive credentials through an environment variable.

Mitigation: Use scoped organization API keys, rotate or revoke keys when needed, and protect the local configuration file.

Risk: A global npm install persists the dLazy CLI on the host.

Mitigation: Use the pinned npx invocation or a sandboxed environment when a persistent global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from dLazy and may reference uploaded files by URL within project-scoped chat sessions.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
