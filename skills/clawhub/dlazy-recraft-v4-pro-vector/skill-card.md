## Description:

High-fidelity text-to-vector model with 4MP-tier quality for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-fidelity vector image assets through the dLazy Recraft V4 Pro Vector command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected inputs, and generated assets may be sent to dLazy hosted services.

Mitigation: Avoid sending sensitive prompts or files unless the user trusts the dLazy service and account terms.

Risk: Authentication stores a dLazy API key locally for CLI use.

Mitigation: Use environment-scoped credentials when preferred, rotate or revoke keys from the dLazy dashboard, and protect the local configuration file.

Risk: The skill uses an external pinned npm CLI package.

Mitigation: Review the pinned package before installing globally, or run the pinned npx command for on-demand use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [JSON response with generated asset URLs and optional local files when saved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task metadata when no-wait mode is used.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
