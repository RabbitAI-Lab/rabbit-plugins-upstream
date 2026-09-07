## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to generate short MiniMax Hailuo video clips through the dLazy CLI, including text-to-video, frame-transition, and multi-reference workflows. It is useful when an agent needs to prepare commands, pass approved prompts or media inputs, and return generated media URLs or saved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly supplied image, video, or audio files are sent to dLazy cloud services for generation.

Mitigation: Use only prompts and media approved for external processing, and review the service terms before handling sensitive or restricted content.

Risk: The CLI uses a dLazy API key, and exposed credentials could allow unauthorized use of the user's organization account.

Mitigation: Use revocable API keys, store them with user-only permissions or pass them per invocation, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing a third-party CLI introduces normal package supply-chain risk.

Mitigation: Prefer the pinned npx invocation when a persistent global install is unnecessary, and review the linked source and npm package before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON responses with generated media URLs, plus optional saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async invocations may return a generateId for later polling; authenticated use requires a dLazy API key.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
