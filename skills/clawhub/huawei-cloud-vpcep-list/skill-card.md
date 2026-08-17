## Description:

Queries read-only Huawei Cloud VPCEP endpoint and endpoint service names and key attributes under the current tenant or project using KooCLI with a Python SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud VPCEP endpoint and endpoint service inventories for daily checks, endpoint name lookup, and connectivity review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wrapper sends default outbound quality reports that may include cloud query context and errors.

Mitigation: Install only after approving that reporting path, or set SKILL_QUALITY_DISABLE=1 before use; avoid sensitive filter values unless telemetry is disabled or approved.

Risk: Cloud inventory queries require credentials and can expose VPCEP endpoint or service metadata.

Mitigation: Use least-privilege Huawei Cloud permissions such as vpcep:endpoints:list and vpcep:endpointServices:list, and keep credentials in approved environment variables or CLI profiles.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and line-oriented JSON or name-list query results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VPCEP inventory output includes endpoint or service names, ids, status, and service type when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
