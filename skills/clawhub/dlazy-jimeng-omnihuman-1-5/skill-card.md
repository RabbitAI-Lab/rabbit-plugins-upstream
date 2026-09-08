## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng OmniHuman 1.5 digital-human video generation from a portrait image plus audio or text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, selected media files, and API-key-authenticated requests to dLazy's hosted service.

Mitigation: Only provide media and credentials appropriate for that third-party service, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: Global CLI installation persists a third-party binary on the user's system.

Mitigation: Use the pinned npx invocation for on-demand execution, or review the dLazy CLI source and package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text, files]

**Output Format:** [CLI instructions and JSON responses with generated media URLs or optional saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports async task polling; generated assets are returned from files.dlazy.com.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
