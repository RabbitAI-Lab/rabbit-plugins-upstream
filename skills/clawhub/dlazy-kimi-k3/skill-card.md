## Description:

Uses a hosted Kimi K3 model for complex analysis, coding, and writing with text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to generate writing, code, or analysis from prompts and optional image or video inputs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media passed to the CLI may be sent to dLazy's hosted service.

Mitigation: Share only prompts and media you are comfortable sending to dLazy; review files before passing their paths.

Risk: Persistent login stores a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY if local credential persistence is undesirable, and rotate or revoke keys when needed.

Risk: The skill relies on a third-party npm CLI and hosted service.

Mitigation: Review the CLI and service before installation; use the documented pinned, on-demand npx command if a global install is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [JSON response containing generated content for the agent to relay]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier instead of immediate content; the documented CLI install is pinned to 1.2.3.]

## Skill Version(s):

1.2.20 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
