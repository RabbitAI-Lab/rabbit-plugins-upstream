## Description:

Query Huawei Cloud SWR image repositories in the current project and region, with optional namespace, repository-name, category, pagination, and sorting filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inspect Huawei Cloud SWR repository inventory, visibility, image counts, paths, and timestamps for daily review or troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials or long-lived profile details may be exposed if pasted into shared terminals or chat.

Mitigation: Use an existing protected hcloud profile or short-lived credentials, and do not ask for or echo AK/SK values.

Risk: Using broad cloud permissions for repository inventory can expose more SWR data than needed.

Mitigation: Use a least-privilege Huawei Cloud IAM identity limited to SWR read access, such as swr:repository:list.

## Reference(s):

- [Huawei Cloud SWR Repository List Skill](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-swr-list)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud SWR listing guidance with optional Python SDK fallback.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
