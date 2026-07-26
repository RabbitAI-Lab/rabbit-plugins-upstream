## Description: <br>
Diagnoses Alibaba Cloud ECS and VPC public network connectivity failures by running bundled read-only troubleshooting scripts for ECS, security groups, NAT gateways, SNAT, routes, EIPs, DDoS status, and Cloud Firewall checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operations engineers and support teams use this skill to diagnose public connectivity failures for a named Alibaba Cloud ECS instance or VPC cloud service VSwitch. The skill produces a diagnostic table and remediation guidance that should be reviewed before making network or security changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Alibaba Cloud credentials are read from standard sources and persisted to scripts/.sts_cache.json. <br>
Mitigation: Use temporary STS credentials or a narrowly scoped read-only RAM role, keep the credential cache protected, and delete the cache after diagnostics. <br>
Risk: Suggested firewall, route, NAT, SNAT, security-group, or gateway changes can alter network exposure. <br>
Mitigation: Treat remediation output as manual guidance; require human review, change approval, and a rollback plan before applying changes. <br>
Risk: The skill makes Alibaba Cloud API calls against user-specified cloud resources. <br>
Mitigation: Confirm the target resource, region, and read-only diagnostic scope before execution, and do not expand beyond the confirmed resource. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-ecs-vpc-publicnetwork-troubleshoot) <br>
- [Module 1: Preparation](artifact/references/module1_preparation.md) <br>
- [Module 2: ECS Public Network](artifact/references/module2_ecs_public.md) <br>
- [Module 3: VPC Service Public Network](artifact/references/module3_vpc_service.md) <br>
- [Module 4: Output and Judgment](artifact/references/module4_output.md) <br>
- [Module 5: Solutions](artifact/references/module5_solution.md) <br>
- [RAM Policies](artifact/references/ram-policies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown diagnostic report with JSON-derived findings, status tables, shell command invocations, and remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user scope confirmation before read-only Alibaba Cloud API calls; aborts on missing parameters, credential failures, or script errors.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
