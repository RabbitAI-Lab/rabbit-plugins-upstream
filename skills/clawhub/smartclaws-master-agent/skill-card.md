## Description:

Run one SmartClaws master control cycle: read device telemetry on-chain, decide under the owner's guidelines, command a device only when allowed, and log the decision on-chain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eduv09](https://clawhub.ai/user/eduv09)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run a single SmartClaws control cycle that reads device telemetry, applies the owner's configured goal and authority rules, optionally issues one authorized command, and logs the outcome on-chain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can command configured devices through SmartClaws when owner configuration permits it.

Mitigation: Install it only in a workspace you control, review SMARTCLAWS.md and AGENTS.md, and keep commandable devices and caller permissions narrow.

Risk: SmartClaws writes, disclosures, and notifications may spend wallet funds and create permanent on-chain records.

Mitigation: Review wallet funding and write authority before use, and publish or disclose only when the owner configuration and task justify it.

Risk: Encrypted channel disclosure may expose plaintext telemetry or messages to the agent.

Mitigation: Use disclosure only for channels where the wallet is an authorized reader and the workflow requires plaintext for the control decision.

Risk: Missing goals, stale telemetry, malformed payloads, or incomplete device wiring can lead to unsafe or unsupported actions.

Mitigation: Stop or ask the owner when SMARTCLAWS.md lacks a goal, required device channels are missing, telemetry is stale, or a device contract does not validate the payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-master-agent)
- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown status report with SmartClaws tool calls and structured on-chain messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transaction hashes when SmartClaws publish or notify operations succeed.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
