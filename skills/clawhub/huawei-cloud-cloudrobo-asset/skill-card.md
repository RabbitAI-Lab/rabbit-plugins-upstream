## Description:

Manage the CloudRobo asset lifecycle, including repository and catalog queries, asset and version CRUD, tag and Action management, permission checks, marketplace search, lineage queries, and local-to-OBS import and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage CloudRobo assets and versions through CLI, SDK, and API workflows, including import/export, metadata validation, permission checks, marketplace discovery, and cleanup operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses AK/SK credentials that can access CloudRobo asset services and OBS import/export endpoints.

Mitigation: Use least-privilege credentials, prefer environment variables over stored config where practical, and protect ~/.cloudrobo/config.yaml if it is used.

Risk: Delete, batch-delete, import, export, create, and update operations can change cloud assets or transfer asset data.

Mitigation: Require explicit user confirmation for mutating operations and use available dry-run modes before execution.

Risk: Disabling SSL verification or enabling request/response traffic logging can expose credentials or sensitive asset data.

Mitigation: Keep SSL verification enabled in production and disable traffic logging except during controlled debugging.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-asset)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [API Paths](references/api-paths.md)
- [Validation Rules](references/validation-rules.md)
- [Edge Cases](references/edge-cases.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI and SDK command examples, JSON parameter examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudRobo CLI commands and dry-run flows; mutating operations require explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
