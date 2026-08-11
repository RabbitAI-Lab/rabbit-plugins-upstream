## Description:

Switch Hermes between buying from the asale market and using its own subscription, and identify running sessions that still use the old configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and switch Hermes configuration between the user's own subscription and asale market buying through a local daemon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install path executes an unpinned remote script.

Mitigation: Review the installer before use and prefer a verified package-manager or pinned install path when available.

Risk: The skill can switch Hermes into paid market buying.

Mitigation: Confirm the desired model selection and buying mode with the user before enabling market buying.

Risk: The skill reads a local daemon token and changes Hermes configuration.

Mitigation: Use it only with a trusted asale daemon and verify changed configuration through the daemon or app after switching.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-hermes)
- [asale homepage](https://asale.ai)
- [asale source repository](https://github.com/asale-ai/asale)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local daemon RPC calls and Hermes configuration state reported by the daemon.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
