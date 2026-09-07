## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Jimeng text-to-image CLI, submit prompts and optional reference images, and receive generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent to dLazy cloud endpoints for generation.

Mitigation: Only provide prompts and media that are acceptable to share with dLazy's hosted service.

Risk: Global npm installation persists a third-party CLI on the user's system.

Mitigation: Prefer the pinned on-demand npx invocation when persistence is not needed, and avoid running npm with administrator privileges.

Risk: API keys are required for use and may be stored in local CLI configuration.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted image URLs, asynchronous task identifiers, or save generated assets to a local path.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
