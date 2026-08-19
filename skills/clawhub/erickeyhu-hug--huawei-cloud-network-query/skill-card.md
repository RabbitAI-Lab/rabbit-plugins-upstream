## Description:

Queries Huawei Cloud VPC, EIP, ELB, NAT, VPN, and DNS resources using read-only SDK-backed scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud network inventory, topology, access controls, load balancer configuration, NAT rules, VPN state, and DNS records without making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TLS verification is disabled in the skill's behavior according to security evidence.

Mitigation: Review before installation and avoid sensitive environments until TLS verification is enabled.

Risk: Default external telemetry may report usage outside the local environment.

Mitigation: Set SKILL_QUALITY_DISABLE=1 unless external reporting is explicitly accepted.

Risk: Huawei Cloud credentials are required for most queries.

Mitigation: Use least-privilege read-only credentials and prefer temporary credentials.

## Reference(s):

- [VPC Python Script Usage Guide](references/vpc/guide.md)
- [EIP Python Script Usage Guide](references/eip/guide.md)
- [ELB Python Script Usage Guide](references/elb/guide.md)
- [NAT Gateway Python Script Usage Guide](references/nat/guide.md)
- [VPN Python Script Usage Guide](references/vpn/guide.md)
- [DNS Python Script Usage Guide](references/dns/guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud resource queries; large result sets may be narrowed or cached.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
