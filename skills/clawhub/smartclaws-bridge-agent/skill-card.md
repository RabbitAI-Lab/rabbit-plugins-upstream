## Description:

Run one SmartClaws bridge cycle for a single device by reading local hardware or APIs, validating against the device contract, publishing telemetry on-chain, and applying validated on-chain commands only in command-enabled modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eduv09](https://clawhub.ai/user/eduv09)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this agent skill to run a single SmartClaws telemetry bridge cycle for one configured device. It can publish validated readings and, when explicitly configured, process validated incoming commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can interact with a configured SmartClaws device and wallet.

Mitigation: Review SMARTCLAWS.md, AGENTS.md, bridge mode, reader keys, and the device contract before installation and use.

Risk: Command-enabled modes can apply incoming device commands.

Mitigation: Use telemetry-only mode unless command handling is intended, and apply commands only after device contract validation.

## Reference(s):

- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws)
- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-bridge-agent)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown or plain text status with SmartClaws plugin calls and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured SmartClaws plugin, SMARTCLAWS.md, AGENTS.md, and one device contract skill.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
