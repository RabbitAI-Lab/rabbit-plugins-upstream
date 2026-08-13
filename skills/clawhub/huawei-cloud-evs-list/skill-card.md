## Description:

Queries Huawei Cloud EVS disk inventories for the current tenant or project and returns disk names with IDs, status, and size, with optional name-only, status, name, and pagination filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inspect Huawei Cloud EVS disk inventory, retrieve EVS disk names, and support daily checks or cost review without changing disk resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads EVS disk names, IDs, status, and size from a Huawei Cloud tenant.

Mitigation: Use a least-privilege IAM credential limited to evs:volumes:list and avoid production or administrator keys.

Risk: CLI and SDK installation commands are executed in the user's environment.

Mitigation: Review installation commands and package sources before running them.

Risk: Invalid EVS status filters can return an empty successful response that resembles no matching disks.

Mitigation: Validate status filters against the documented EVS enum before reporting an empty result as authoritative.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-evs-list)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tabular EVS disk summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return detailed disk fields or a name-only list; command outputs are read-only EVS list results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
