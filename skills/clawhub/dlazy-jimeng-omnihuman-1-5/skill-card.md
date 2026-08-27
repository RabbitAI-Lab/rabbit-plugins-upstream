## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the dLazy CLI for generating digital human broadcast videos from a portrait image plus audio or text prompt. It supports synchronous generation, asynchronous task polling, and saving generated media assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and provided image or audio files are sent to dLazy cloud endpoints for generation.

Mitigation: Only pass media, prompts, and files that are appropriate to upload to dLazy's service.

Risk: The skill depends on a third-party CLI and cloud API.

Mitigation: Use the pinned npx invocation when avoiding a persistent global install, and review the third-party CLI source when higher assurance is required.

Risk: Authentication uses a dLazy API key that may be saved in local CLI configuration.

Mitigation: Prefer per-invocation environment variables when appropriate, and rotate or revoke keys from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated media URLs or saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a task identifier for later polling; generated assets are hosted on files.dlazy.com or saved to a requested local path.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
