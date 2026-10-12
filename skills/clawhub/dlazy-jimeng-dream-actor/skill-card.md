## Description:

Helps turn a static character image into an action video using Jimeng Dream Actor through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to animate character images with prompts and optional reference video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chosen images, videos, and prompts are sent to dLazy's cloud service.

Mitigation: Confirm before uploading private media and use only content approved for the service.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the key and rotate or revoke it when access is no longer needed.

Risk: A global CLI installation persists on the user's machine.

Mitigation: Use the pinned on-demand npx invocation when a persistent installation is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a hosted result URL or an asynchronous task ID; results can optionally be saved locally.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
