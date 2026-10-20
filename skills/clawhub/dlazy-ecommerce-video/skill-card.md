## Description:

Turns product images, documents, or listing links into ecommerce advertising videos with multilingual voiceover and an optional digital presenter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketers use this skill to create product ads and shopping videos from product materials or store listing links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the third-party dLazy service.

Mitigation: Review materials before submission and avoid uploading confidential content without approval.

Risk: Login stores an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

Risk: Using the skill installs or runs a third-party npm CLI.

Mitigation: Review the package before running it; use the documented pinned npx command to avoid a global installation.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streamed text from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service handles video generation and maintains project context across sessions.]

## Skill Version(s):

1.0.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
