## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy's Vidu Audio Clone workflow, supplying a reference audio URL or local audio path and prompt to generate cloned-voice reading audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads prompts and audio inputs to dLazy's hosted service.

Mitigation: Only pass audio files, URLs, and prompts that are appropriate to share with dLazy, and review the service terms before use.

Risk: The skill requires dLazy API credentials that could be exposed through local configuration or environment handling.

Mitigation: Use a revocable API key, keep local configuration access limited to the current user, and rotate the key if exposure is suspected.

Risk: Global npm installation persists the dLazy CLI binary on the system.

Mitigation: Confirm trust in dLazy and the @dlazy/cli npm package before installing, or use the npx invocation path for non-persistent execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI to call hosted API endpoints and may return generated media URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
