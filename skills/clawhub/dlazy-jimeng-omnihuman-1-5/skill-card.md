## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to invoke the dLazy CLI for creating digital-human broadcast videos from a portrait image plus prompt text or audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, portrait images, audio, and generated media data to dLazy cloud services.

Mitigation: Use only content that is appropriate for processing by dLazy, and avoid sensitive media unless the user accepts that cloud-processing posture.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for per-invocation authentication when persistence is not desired, and rotate or revoke keys from the dLazy dashboard after exposure or on shared machines.

Risk: The skill depends on a third-party CLI and hosted API endpoints for generation.

Mitigation: Review the pinned CLI package and source before installation, and verify user account access, balance, and API availability before relying on it in a workflow.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or a locally saved generated asset when requested.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
