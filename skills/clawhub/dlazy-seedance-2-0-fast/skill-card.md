## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos from prompts, media references, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Seedance 2.0 Fast video generation service from an agent workflow. It supports text-to-video, multi-modal references, and first/last-frame guided generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths provided to the skill are sent to dLazy-hosted services for generation.

Mitigation: Do not submit confidential prompts or sensitive media unless the intended use permits sending them to dLazy's API and media storage.

Risk: The skill uses a third-party npm CLI package that may be installed globally.

Mitigation: Review @dlazy/cli before use and prefer npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not desired.

Risk: API keys may be saved in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI returns JSON containing generated media URLs, task status for asynchronous runs, and optional saved output paths.]

## Skill Version(s):

1.3.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
