## Description:

Generates coherent transition videos from first and last frame images using Jimeng's first-tail frame model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent call dLazy's Jimeng first-tail frame workflow and generate a transition video from a prompt plus first and last frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm CLI and sends selected prompts and media files to dLazy hosted API endpoints.

Mitigation: Install only when the publisher is trusted, prefer on-demand npx use, review the referenced CLI package before use, and confirm which local files will be uploaded.

Risk: The CLI stores or receives a dLazy API key for authenticated calls.

Mitigation: Use a revocable API key, rotate or revoke it when no longer needed, and prefer per-invocation environment variables when persistent local storage is not desired.

Risk: The security verdict is suspicious because the skill combines cloud media upload, local credential storage, and forceful billing/authentication instructions.

Mitigation: Review dLazy account, billing, and authentication prompts before invocation, use dry-run where available, and do not let the skill proceed with unexpected charges or uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI repository link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with bash commands; CLI responses are JSON with generated media URLs and optional downloaded result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, asynchronous task IDs, polling, timeouts, and saving generated assets to a local path.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
