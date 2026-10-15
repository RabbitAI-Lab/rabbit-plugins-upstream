## Description:

Helps agents generate digital-human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to create digital-human presenter videos from a portrait and audio or text through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, audio, or video files may be uploaded to dLazy, and generated results are hosted there.

Mitigation: Submit only media and prompts approved for the hosted service; review dLazy's terms before use.

Risk: Signing in can save an API key in local CLI configuration.

Mitigation: Protect local credentials or supply the key per invocation; rotate or revoke it if exposed.

Risk: Generation may consume paid credits or leave a globally installed CLI.

Mitigation: Use dry-run for a cost estimate and the pinned npx invocation when a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON responses, Video links]

**Output Format:** [Markdown instructions and CLI JSON responses with hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task identifier and local result download.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
