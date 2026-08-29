## Description:

Audio generation skill that automatically selects an appropriate dLazy CLI audio or text-to-speech model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate speech, music, sound effects, and other audio through dLazy's hosted CLI and API models from natural-language prompts and selected parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local files passed as inputs may be sent to dLazy's hosted service.

Mitigation: Use only content appropriate for that service and avoid sending sensitive files unless the user has approved the data handling.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use per-invocation credentials or the npx alternative when persistence is not desired, and rotate or revoke keys when needed.

Risk: Generated media URLs are hosted by dLazy's file service.

Mitigation: Treat returned URLs as externally hosted outputs and avoid exposing confidential generated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI invocations return JSON envelopes and generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned @dlazy/cli install spec and may require a dLazy API key.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
