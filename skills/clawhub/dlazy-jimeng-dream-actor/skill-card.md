## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a static character image, optional reference media, and a prompt into a Jimeng Dream Actor action-video generation request through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, local media paths, and generated outputs through the dLazy hosted service.

Mitigation: Use it only for content you are comfortable processing with dLazy, and confirm before submitting sensitive images, videos, prompts, or credentials.

Risk: The skill depends on the npm/npx-installed dLazy CLI and external endpoints.

Mitigation: Install the pinned CLI version from the skill metadata and review the package/source links before use.

Risk: Broad image-to-video trigger phrases could route unrelated work to this third-party service.

Mitigation: Invoke the skill only for explicit Jimeng Dream Actor requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses from the dLazy CLI, with optional downloaded generated media files when a save path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers for later polling when no-wait mode is used.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
