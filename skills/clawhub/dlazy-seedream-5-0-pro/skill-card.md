## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Seedream 5.0 Pro image-generation CLI for high-detail commercial key visuals, typography-sensitive images, complex compositions, and brand assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm package and dLazy cloud API.

Mitigation: Install only if the publisher and @dlazy/cli package are trusted; use the pinned npx invocation when a persistent global install is not desired.

Risk: Prompts, parameters, and local image paths passed to the CLI may be sent or uploaded to dLazy services.

Mitigation: Pass only files intended for upload and avoid submitting sensitive content unless the user's dLazy account and service terms are appropriate for that data.

Risk: Saved API keys can persist in the local dLazy configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY for ephemeral use, and rotate or revoke organization API keys from the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, local saved image files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.2.9 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
