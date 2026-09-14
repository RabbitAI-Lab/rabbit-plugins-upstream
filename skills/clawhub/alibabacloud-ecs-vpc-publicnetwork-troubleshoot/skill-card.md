## Description:

Diagnoses Alibaba Cloud ECS public network access and VPC cloud service egress failures, including public IP reachability, security group blocking, NAT gateway, SNAT, route, and EIP checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to diagnose public connectivity failures for Alibaba Cloud ECS instances and VPC-hosted services such as DataWorks, SAE, and ACK. It guides read-only checks for account status, security groups, ACLs, routes, NAT/SNAT, EIP, DDoS, and Cloud Firewall signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Alibaba Cloud credentials and writes reusable credentials to scripts/.sts_cache.json.

Mitigation: Use a least-privilege read-only RAM role, prefer short-lived STS credentials, and clear the cache after use.

Risk: Cached credentials can be reused across runs and may make the active account ambiguous.

Mitigation: Verify the account identity before trusting results and refresh or remove cached credentials when switching accounts.

Risk: A Normal result with execution notes or errors can represent a degraded or skipped check rather than a confirmed healthy state.

Mitigation: Review execution notes and treat degraded checks as incomplete until the missing prerequisite is resolved and the diagnostic is rerun.

## Reference(s):

- [Preparation](references/module1_preparation.md)
- [RAM Permission Declaration](references/ram-policies.md)
- [Scenario 1: ECS Instance Public Network Access/Inbound Failure](references/module2_ecs_public.md)
- [Scenario 2: VPC Cloud Service Cannot Access Public Network](references/module3_vpc_service.md)
- [Output Results and Determination Specification](references/module4_output.md)
- [Solution Module](references/module5_solution.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnostic tables with inline shell commands and remediation steps; bundled scripts emit JSON used to form the report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires region_id plus either instance_id or vswitch_id; may include execution notes when checks are degraded or skipped.]

## Skill Version(s):

0.0.2 (source: server release evidence and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
