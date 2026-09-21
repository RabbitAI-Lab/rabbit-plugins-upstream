## Description:

Query Huawei Cloud VPCEP (VPC Endpoint) names by keyword, and list all VPC Endpoints across a region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud VPCEP endpoint names, statuses, VPCs, IPs, and creation times across a selected region. It supports read-only inventory reporting, fuzzy endpoint-name lookup, and paginated browsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials may be exposed through shell history, shared terminals, or local configuration during Huawei Cloud authentication.

Mitigation: Use environment variables or secure CLI configuration, avoid pasting real AK/SK values into shared sessions, and rotate credentials if exposure is suspected.

Risk: Over-broad IAM permissions can expose more VPCEP resources than the lookup task requires.

Mitigation: Use the documented least-privilege vpcep:endpoints:list permission or VPCEP ReadOnlyAccess, and do not grant create, modify, or delete permissions for this skill.

Risk: Installing hcloud with sudo from a downloaded archive can introduce supply-chain risk if the source is not verified.

Mitigation: Download hcloud only from the documented Huawei Cloud source and verify the download source before moving the binary into a system path.

Risk: Queries against the wrong region can produce incomplete or misleading endpoint inventory.

Mitigation: Confirm the target Huawei Cloud region before execution and set the region explicitly in CLI or SDK commands.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-vpcep-name-list)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VPCEP query guidance with CLI-first execution and Python SDK fallback.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
