## Description:

Synthesize text into natural, fluent speech with Doubao TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to synthesize text prompts into hosted Doubao TTS speech outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends synthesis prompts, selected parameters, and any referenced local media to dLazy cloud endpoints.

Mitigation: Install only when that data sharing is acceptable; prefer per-invocation DLAZY_API_KEY or npx when avoiding persistent global setup.

Risk: Broad trigger keywords could lead an agent to invoke a paid external API unintentionally.

Mitigation: Use explicit invocations such as "doubao tts" or "dlazy doubao-tts" and review usage before automation.

Risk: The documented speech-tool output schema includes image/PNG examples that may not match actual TTS output.

Mitigation: Verify the real output schema before wiring the skill into downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files]

**Output Format:** [CLI guidance and JSON responses with generated output URLs; async calls may return a task identifier for polling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; can use a pinned global install or npx invocation of @dlazy/cli@1.2.3.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
