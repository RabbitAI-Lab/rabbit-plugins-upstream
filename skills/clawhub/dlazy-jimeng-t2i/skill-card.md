## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Jimeng text-to-image generation through the pinned dLazy CLI, with support for prompts, optional reference images, and asynchronous task polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local files supplied as inputs may be sent to dLazy's hosted service for generation.

Mitigation: Use only prompts and files appropriate for the dLazy provider, and avoid submitting sensitive content unless that use is approved.

Risk: The dLazy CLI can save an API key in the local user configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for less persistent use, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Image URLs]

**Output Format:** [Markdown guidance with CLI commands; command output is JSON containing generated image URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; the CLI can store credentials locally or read DLAZY_API_KEY per invocation.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
