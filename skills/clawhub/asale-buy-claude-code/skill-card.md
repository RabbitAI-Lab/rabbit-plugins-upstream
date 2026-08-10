## Description:

Switches Claude Code between buying from the asale market and using its own subscription, and reports which running sessions still use the previous configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Claude Code use this skill to inspect and switch whether future Claude Code sessions route through the local asale market proxy or their own subscription, while identifying running sessions that still use the prior configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install path runs a remote script with full shell privileges.

Mitigation: Review the installer source and publisher trust before installing or updating the asale daemon.

Risk: Enabling the switch changes future Claude Code traffic and credentials to use asale's local proxy and market flow.

Mitigation: Confirm the user's intent before enabling the switch, run the documented status check first, and tell the user that existing sessions keep their previous configuration until restart.

Risk: The skill reads a local daemon token and requires a signed-in asale account for buying.

Mitigation: Use only the loopback daemon endpoint with the token header, and stop on sign-in or authorization errors instead of retrying or bypassing the account requirement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-claude-code)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [asale homepage](https://asale.ai)
- [asale source repository](https://github.com/asale-ai/asale)
- [asale Unix installer](https://asale.ai/dl/install.sh)
- [asale Windows installer](https://asale.ai/dl/install.ps1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON RPC examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local daemon calls and Claude Code configuration switching; does not itself produce persistent output files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
