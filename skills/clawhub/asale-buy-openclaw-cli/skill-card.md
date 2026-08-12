## Description:

Switches OpenClaw between buying from the asale market and using its own subscription, and helps identify running OpenClaw sessions still using the previous configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to inspect the asale buy-switch state, choose market models, toggle OpenClaw's local configuration, and understand which already-running sessions still use the previous configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install commands execute remote scripts with local user privileges.

Mitigation: Review the asale installer source and trust boundary before running the install commands.

Risk: The skill can change local OpenClaw configuration through a local daemon token and route future model requests through the asale market.

Mitigation: Use the skill only when you intend to let the asale daemon update OpenClaw configuration, and verify the resulting state with the documented status checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-openclaw-cli)
- [asale homepage](https://asale.ai)
- [asale source link declared in skill metadata](https://github.com/asale-ai/asale)
- [Unix install command URL declared in skill metadata](https://asale.ai/dl/install.sh)
- [Windows install command URL declared in skill metadata](https://asale.ai/dl/install.ps1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local RPC calls to an asale daemon and reports configuration state; it does not directly contact asale servers.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter version: 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
