## Description:

Network AIops helps agents inspect and operate NAPALM-supported network devices, run read-only RCA, back up and diff configs, and perform governed config changes with optional NetBox lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network engineers, and operators use this skill to inspect device state, diagnose interface or BGP issues, back up and diff configurations, and perform reviewed network changes across Cisco, Arista, and Juniper devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live network device configuration.

Mitigation: Use read-only device credentials by default, require an operator-approved diff before writes, and reserve config-capable credentials for controlled change windows.

Risk: Network credentials or raw running configs can be exposed through environment variables or transcripts.

Mitigation: Use the encrypted secret store, avoid long-lived exported master passwords, keep enable secrets out of config.yaml, and avoid sending include_secrets=True output through an agent transcript.

Risk: A config replace or management-plane change can lock operators out of a device.

Mitigation: Prefer dry-run diffs first, use device-side revert timers where supported, verify reachability from a new session before confirming, and arrange out-of-band access for high-risk changes.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Network-AIops)
- [network-aiops Capabilities](references/capabilities.md)
- [network-aiops CLI Reference](references/cli-reference.md)
- [network-aiops Setup Guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and summarized tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network command and configuration outputs may be redacted, size-bounded, or represented as structured fields.]

## Skill Version(s):

0.12.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
