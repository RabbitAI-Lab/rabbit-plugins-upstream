## Description:

ByteDance's Seedance 2.0 video generation skill uses the dLazy CLI and hosted API to generate videos from text prompts, reference images, video, audio, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke Seedance 2.0 through the pinned dLazy CLI for text-to-video, multi-modal reference video generation, and first/last-frame workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted API and media storage.

Mitigation: Use only content appropriate for that service, and avoid submitting sensitive media unless the account and service terms permit it.

Risk: The skill depends on a pinned third-party npm CLI that can be installed globally or run on demand.

Mitigation: Prefer npx or an isolated environment when evaluating the skill, and review the pinned CLI package before global installation.

Risk: A dLazy API key is required and may be stored in the local CLI configuration.

Mitigation: Keep the API key scoped to the intended organization, rotate or revoke it when no longer needed, and use per-invocation environment variables when persistent local storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs, with optional local save paths and asynchronous task IDs when no-wait mode is used.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
