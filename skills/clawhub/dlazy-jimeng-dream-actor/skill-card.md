## Description:

Guides agents to turn a character image into an action video with Jimeng Dream Actor through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating action videos from character images and prompts via the dLazy-hosted Jimeng Dream Actor service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted endpoints.

Mitigation: Upload only media and prompts you are comfortable sharing with the third-party service.

Risk: Using the third-party CLI may persist an API key in local configuration.

Mitigation: Review the CLI before installation and use a per-invocation key if local credential storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source (skill metadata; not release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON responses]

**Output Format:** [Text and shell commands; CLI returns JSON with hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID; results can optionally be saved locally.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
