## Description:

Queries Huawei Cloud network resources, including VPC, EIP, ELB, NAT, VPN, and DNS inventory, using read-only operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inventory Huawei Cloud network topology, security rules, load balancers, NAT rules, VPN status, DNS records, and reusable resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup runs local code, creates a virtual environment, and installs Python packages before use.

Mitigation: Review the setup scripts and dependency list before running them, and execute the skill in an isolated workspace or environment.

Risk: Queries require Huawei Cloud access keys and may operate against sensitive cloud accounts.

Mitigation: Use least-privilege read-only credentials, prefer temporary credentials, and avoid exposing HW_ACCESS_KEY, HW_SECRET_KEY, or HW_SECURITY_TOKEN in outputs.

Risk: Security evidence flags TLS verification and get-pip bootstrap behavior as concerns.

Mitigation: Review or correct TLS verification and bootstrap behavior before using the skill with production credentials or sensitive accounts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-network-query)
- [VPC query guide](references/vpc/guide.md)
- [EIP query guide](references/eip/guide.md)
- [ELB query guide](references/elb/guide.md)
- [NAT query guide](references/nat/guide.md)
- [VPN query guide](references/vpn/guide.md)
- [DNS query guide](references/dns/guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON query results from Huawei Cloud SDK scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud credentials in environment variables and may create a local Python virtual environment during setup.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
