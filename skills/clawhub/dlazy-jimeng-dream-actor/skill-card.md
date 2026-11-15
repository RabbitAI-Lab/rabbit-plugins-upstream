## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can turn a static character image into an action video by providing a prompt and image to the Jimeng Dream Actor service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence but partial coverage; it flags the login step's connection to video generation as unclear.

Mitigation: Review the full skill and referenced CLI material, and confirm you trust dLazy's login flow before installing or authenticating.

Risk: Prompts and local media supplied for generation are sent to dLazy-hosted services.

Mitigation: Submit only content approved for cloud processing.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON result with a hosted generated video URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return asynchronously with a task identifier.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
