## Description:

Tongyi Wanxiang 2.7 video generation skill for text-to-video, first/last-frame-to-video, and reference-based video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Wan 2.7 video generation workflow from an agent, supplying prompts and optional media for text-to-video, first/last-frame-to-video, or reference-based generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded local media are sent to dLazy's hosted API and media storage.

Mitigation: Use only data approved for third-party processing, and avoid sensitive inputs unless permitted by the user's policy.

Risk: API keys can be saved in the local dLazy CLI config when using login or auth set.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when a saved local key is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy command on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown instructions with bash command examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return generated output URLs or an asynchronous generateId for polling.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
