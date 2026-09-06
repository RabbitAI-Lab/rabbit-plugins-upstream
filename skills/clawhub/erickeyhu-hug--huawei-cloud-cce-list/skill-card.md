## Description:

Queries Huawei Cloud CCE cluster lists for the current tenant or project and returns cluster names, IDs, status, version, and flavor using KooCLI with an SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and platform engineers use this skill to inspect Huawei Cloud CCE cluster inventory, produce cluster-name lists, and review cluster status, version, and flavor without creating, modifying, or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented read-only boundary conflicts with an optional detail mode that may expose node or addon metadata.

Mitigation: Install only after reviewing the detail-mode behavior, and use the skill for cluster-list and cluster-name inventory unless node or addon metadata exposure is explicitly intended.

Risk: A broad read-only role can expose more CCE metadata than the cluster-list workflow requires.

Mitigation: Use the fine-grained cce:cluster:list permission where possible instead of the broader CCE ReadOnlyAccess policy.

Risk: The skill depends on Huawei Cloud credentials and region configuration.

Mitigation: Keep access keys out of files, prefer environment or CLI credential storage, and confirm the target region before running list commands.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Skill Gate Report](references/skill-gate-report.txt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CCE cluster listing; requires authenticated Huawei Cloud credentials, region selection, and least-privilege CCE list permission.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
