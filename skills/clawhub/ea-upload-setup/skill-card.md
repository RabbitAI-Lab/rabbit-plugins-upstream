## Description:

Standardized EA deployment for MT5: copy, compile, restart, verify. One command to deploy your MetaTrader Expert Advisor and confirm it is running with heartbeat verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy a MetaTrader 5 Expert Advisor, compile it, restart the trading service, and verify that it is running with a fresh heartbeat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment steps can change files in a live MetaTrader 5 installation and restart mt5.service, which may interrupt or alter live trading behavior.

Mitigation: Require explicit operator confirmation before deployment, review deploy_ea.sh in the target workspace first, and verify service health and heartbeat after changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/ea-upload-setup)
- [Publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit operator confirmation before state-changing deployment steps.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
