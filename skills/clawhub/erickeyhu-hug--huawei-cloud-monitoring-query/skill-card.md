## Description:

Queries Huawei Cloud CES and EPS resources, including alarm rules, alarm histories, templates, dashboards, notification masks, resource groups, one-click alarms, and enterprise project information, using read-only local Python scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud monitoring and enterprise project state for status checks, inventory, dashboard review, alarm investigation, and automation parameter discovery. It is limited to read-only CES and EPS queries and should not be used for creating, modifying, or deleting cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports disabled HTTPS certificate verification while using cloud credentials and installing dependencies.

Mitigation: Review before installing, use a least-privilege Huawei Cloud account, avoid long-lived AK/SK credentials when possible, and prefer a version that keeps certificate verification enabled and pins dependencies.

Risk: The skill requires Huawei Cloud credentials and can expose account metadata through query output if used with broad permissions.

Mitigation: Use CES ReadOnlyAccess and EPS ReadOnlyAccess, grant IAM lookup permissions only when automatic project ID resolution is needed, and do not print credential environment variable values.

## Reference(s):

- [CES Python Script Usage Guide](references/ces/guide.md)
- [Enterprise Project EPS Python Script Usage Guide](references/eps/guide.md)
- [IAM Policies](references/iam-policies.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-monitoring-query)
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON-formatted query results from local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud CES/EPS query output; result fields vary by selected script and cloud API response.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
