## Description:

Helps agents create Kling V3 videos from text prompts or reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text prompts or reference images, with options for aspect ratio, duration, sound, and quality mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media can be sent to dLazy's cloud service, and generated media is hosted there.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy; review the service terms before use.

Risk: Signing in may store an API key locally.

Mitigation: Protect local credentials and rotate or revoke keys through the dLazy dashboard when needed.

Risk: A global CLI install persists on the user's system.

Mitigation: Use the pinned npx invocation if you prefer not to install the CLI globally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video links]

**Output Format:** [Markdown guidance and JSON results with hosted media URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional download of generated media to a local path.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
