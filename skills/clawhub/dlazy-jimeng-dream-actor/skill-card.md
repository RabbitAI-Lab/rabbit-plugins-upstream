## Description:

Helps turn a static character image into an action video using Jimeng Dream Actor through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate action videos from character images and prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Confirm the selected files and use dry-run or explicit approval before uploading sensitive media.

Risk: Generation requests may consume service credits.

Mitigation: Check the dry-run cost estimate before making a paid request.

Risk: CLI login can save an API key in the user's local configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistent local key storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source referenced by skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status or a link to the generated result.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
