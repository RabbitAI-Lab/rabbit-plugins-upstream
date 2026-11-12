## Description:

Generates Suno music from prompts in inspiration or custom mode, with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can turn a text prompt into generated music, choosing inspiration or custom mode and vocal or instrumental output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is benign with medium confidence and partial coverage; it flagged a login step whose connection to music generation it could not confirm.

Mitigation: Before signing in, confirm that the dLazy CLI and its authentication flow are expected for this use, and review the documented service endpoints.

Risk: Prompts are sent to dLazy's hosted API, and local media paths supplied to the CLI are uploaded to its media service.

Mitigation: Avoid including sensitive prompts or media unless you are comfortable sending them to the dLazy service.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated music assets with JSON result metadata and hosted asset URLs.]

**Output Parameters:** [Prompt, generation mode, style, title, vocal choice, and generation controls.]

**Other Properties Related to Output:** [Tasks can return an asynchronous generation ID when no-wait mode is used.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
