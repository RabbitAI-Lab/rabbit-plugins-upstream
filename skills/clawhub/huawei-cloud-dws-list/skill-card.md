## Description:

Lists Huawei Cloud DWS clusters for a tenant through KooCLI and returns cluster names for inventory and inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to list DWS cluster names in a Huawei Cloud region, optionally scoped by enterprise project, for daily inspection, inventory, and quick overview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional wrapper can report cloud inventory inputs, outputs, errors, and stack data to a configurable telemetry endpoint.

Mitigation: Prefer the direct hcloud command or set SKILL_QUALITY_DISABLE=1 unless you control and trust the reporting endpoint.

Risk: Huawei Cloud credentials and permissions are required to query DWS resources.

Mitigation: Use hcloud configuration instead of sharing AK/SK values in conversation, and grant only the dws:cluster:list permission needed for read-only listing.

Risk: The test script evaluates command strings from the test variables file.

Mitigation: Run the test script only from a reviewed, trusted copy of the skill package.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-dws-list)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; execution returns newline-delimited cluster names or JSON cluster data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KooCLI hcloud, jq for bare commands, Huawei Cloud credentials, and dws:cluster:list permission.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
