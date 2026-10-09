## Description:

Helps agents turn a static character image into an action video using Jimeng Dream Actor through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating action videos from character images and text prompts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's external service.

Mitigation: Share only media and prompts you are comfortable uploading to dLazy.

Risk: Logging in may store an API key on the local device.

Mitigation: Use a per-invocation DLAZY_API_KEY if you prefer not to persist the key locally.

Risk: Generation requests may consume account credits.

Mitigation: Check the cost estimate with --dry-run before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell commands and brief guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe returned video URLs or asynchronous task status.]

## Skill Version(s):

1.3.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
