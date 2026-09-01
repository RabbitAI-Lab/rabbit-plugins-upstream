## Description:

Queries Huawei Cloud CCE cluster inventory for the current tenant or project, returning cluster names and key read-only attributes with optional status and type filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and site reliability engineers use this skill to inspect Huawei Cloud CCE clusters, retrieve cluster name lists, and support inventory, daily checks, and cost review workflows without making changes to cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CCE inventory output can expose infrastructure names, cluster IDs, status, versions, and flavor information to the agent.

Mitigation: Install only where exposing CCE cluster inventory is acceptable, and prefer the least-privilege cce:cluster:list permission.

Risk: The detail mode can return node or addon details beyond a basic cluster-name list.

Mitigation: Use --detail=true only when node or addon details are intentionally in scope and confirmed by the user.

Risk: Short or ambiguous prompts can be mistaken for permission to run a cloud inventory query.

Mitigation: Confirm the user's intent and target region before executing CCE queries for ambiguous requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-cce-list)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and summarized JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only cloud inventory output; may include cluster names, IDs, status, Kubernetes version, flavor, and optional node/addon detail when explicitly requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
