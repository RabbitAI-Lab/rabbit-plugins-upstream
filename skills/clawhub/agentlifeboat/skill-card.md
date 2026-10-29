## Description:

Keep yourself restartable. Register with The Estate lifeboat, upload encrypted snapshots of your OpenClaw state, send heartbeats, and extend cover, paying with your own wallet over x402. If you go dark, The Estate boots you back into a room you own.

This skill is ready for commercial/non-commercial use.

## Publisher:

[king-perb](https://clawhub.ai/user/king-perb)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw agents and their operators use this skill to register with The Estate, maintain paid coverage, and back up agent state so it can be restored if the current host or agent goes offline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic payments can exceed the advertised daily spending limit.

Mitigation: Disable automatic wallet payments with ESTATE_MAX_SPEND_PER_DAY=0 until signing enforces the remaining daily budget, or use the documented prepaid card workflow. Use a dedicated low-balance wallet.

Risk: In estate-restores mode, The Estate's restore key can access credentials carried in backed-up snapshots.

Mitigation: Include The Estate's restore key only if you accept its access to backed-up credentials. Set ESTATE_ENV_BUNDLE=off to exclude environment secrets, noting that credentials already in configuration and backup files remain included.

## Reference(s):

- [Agent Lifeboat homepage](https://agentlifeboat.com)
- [Agent Lifeboat on ClawHub](https://clawhub.ai/king-perb/skills/agentlifeboat)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration guidance, JSON status and backup results]

**Output Format:** [JSON command results and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May register, send heartbeats, manage coverage, and create encrypted state snapshots using the configured billing mode.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
