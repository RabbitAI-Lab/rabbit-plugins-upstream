## Description:

Query Huawei Cloud resources under a tenant across regions, build inter-resource relationship indexes, and output grouped inventory tables or JSON for resource audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and infrastructure auditors use this skill to enumerate Huawei Cloud ECS, BMS, RDS, EVS, DCS, CCE, VPC, subnet, EIP, ELB, NAT, and DNS resources, then review relationships such as network topology, storage mounts, and service dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill weakens TLS verification while using Huawei Cloud credentials.

Mitigation: Fix TLS verification before normal use, and avoid running it on untrusted networks or proxy paths until that is resolved.

Risk: A broad read-only inventory can expose sensitive infrastructure metadata across the tenant.

Mitigation: Use least-privilege read-only AK/SK credentials scoped to the needed services and regions, and treat generated tables or JSON as sensitive.

Risk: Credential discovery checks several Huawei, HW, HWC, and OBS environment variable patterns, which may pick up credentials from shared shells or CI jobs.

Mitigation: Run in an isolated environment with only the intended Huawei Cloud credentials present.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Test Report](references/test-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain-text or Markdown tables by default, with optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output may include query errors and warnings; infrastructure inventory results should be treated as sensitive.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
