## Description:

Guides an agent to generate transition videos from first and last frame images using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate a transition video from supplied first- and last-frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external CLI runs third-party package code.

Mitigation: Review the package before installation; use the on-demand npx invocation if a persistent global installation is unnecessary.

Risk: Local media supplied for generation is uploaded to dLazy's hosted service.

Mitigation: Only submit media that you are comfortable sharing with dLazy.

Risk: The CLI can store a dLazy API key locally.

Mitigation: Use a revocable key and rotate or revoke it if its storage or exposure is a concern.

## Reference(s):

- [dLazy CLI repository (linked in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return an asynchronous task ID; completed media can be saved locally.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
