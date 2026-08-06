## Description: <br>
Queries read-only Huawei Cloud network resources across VPC, EIP, ELB, NAT, VPN, and DNS so agents can inspect topology, security rules, load balancing, NAT/VPN status, and DNS records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud or network engineers use this skill to query Huawei Cloud network inventory and configuration from existing accounts. It supports read-only discovery for topology review, security-rule inspection, load balancer and NAT/VPN status checks, DNS record lookup, and reusable resource IDs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup and API calls handle Huawei Cloud credentials while TLS verification is disabled and package bootstrapping can download dependencies from the network. <br>
Mitigation: Review before installing; use isolated environments and temporary, least-privilege, read-only credentials; enable or explicitly control TLS verification; and pin or checksum-verify dependencies before execution. <br>
Risk: Query output can expose private network topology, VPN user and IP details, DNS records, certificate settings, and project identifiers. <br>
Mitigation: Limit access to operators with a need to know, scope queries to required regions and resources, and redact sensitive output before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-network-query) <br>
- [DNS usage guide](references/dns/guide.md) <br>
- [EIP usage guide](references/eip/guide.md) <br>
- [ELB usage guide](references/elb/guide.md) <br>
- [NAT Gateway usage guide](references/nat/guide.md) <br>
- [VPC usage guide](references/vpc/guide.md) <br>
- [VPN usage guide](references/vpn/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query results may contain cloud resource identifiers, network topology, DNS records, certificate metadata, VPN details, and project identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
