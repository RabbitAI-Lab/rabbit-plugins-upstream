## Description:

Helps agents generate transition videos from first and last frame images using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a transition video between supplied first and last frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external CLI package requires trusting its behavior.

Mitigation: Review the pinned dLazy CLI package before installing and check its actual command help before use.

Risk: Prompts and provided local media are sent to dLazy's hosted service.

Mitigation: Only submit content approved for external processing and avoid sensitive media or prompts.

Risk: A saved API key persists in local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when persistent local storage is undesirable.

Risk: Published examples conflict with the documented frame flags and output description.

Mitigation: Verify the installed CLI's help and test the expected result before relying on example commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with CLI commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is returned as a hosted result URL; asynchronous calls can return a generation ID instead.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
