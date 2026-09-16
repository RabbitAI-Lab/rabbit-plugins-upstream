## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Jimeng OmniHuman 1.5 service from an agent workflow to create digital-human broadcast videos from a portrait image with audio or text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and hosted API that require user trust in dLazy and the @dlazy/cli package.

Mitigation: Install only after reviewing the package source and prefer npx when a persistent global install is unnecessary.

Risk: API-key handling can expose credentials if users paste keys into shell history or shared logs.

Mitigation: Prefer the documented device-code login flow or use the DLAZY_API_KEY environment variable only in trusted shells.

Risk: Portrait images, audio, and prompts may be uploaded to dLazy-hosted services for generation.

Mitigation: Do not submit private or sensitive media unless the user is comfortable with upload to dLazy's hosted service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs or an asynchronous generation task identifier.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
