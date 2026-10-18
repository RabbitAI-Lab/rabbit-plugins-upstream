## Description:

Helps operators inspect and troubleshoot VMware NSX networking and make explicitly requested changes to segments, gateways, NAT, routing, and IP pools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and infrastructure engineers use this skill to inspect NSX networking, diagnose connectivity and health, and carry out specific user-requested network changes through NSX Manager.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network changes or deletion can disrupt connected services.

Mitigation: Use an account limited to the required permissions, request explicit approval for each change, preview deletes and dry-run CLI writes, and review dependencies before confirming.

Risk: NSX credentials may be exposed through shell history or long-lived local files.

Mitigation: Use a secret manager or injected environment variables instead of entering production passwords in commands or persistent .env files.

Risk: Bypassing authentication or certificate verification weakens NSX access protections.

Mitigation: Keep certificate verification enabled, trust private CAs as needed, and reserve --skip-auth for temporary diagnostics.

## Reference(s):

- [Skill listing](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-NSX)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with CLI examples and structured NSX tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may be paginated; writes can change live network configuration.]

## Skill Version(s):

1.15.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
