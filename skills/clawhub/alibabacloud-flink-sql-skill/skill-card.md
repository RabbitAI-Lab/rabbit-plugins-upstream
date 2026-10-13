## Description:

Helps engineers author, validate, deploy, operate, and troubleshoot Alibaba Cloud Flink SQL jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Flink developers and operators use this skill to manage SQL job lifecycles and investigate deployment and performance issues in Alibaba Cloud Realtime Compute for Apache Flink.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broadly scoped Flink REST proxy may access privileged diagnostic endpoints despite its read-only label.

Mitigation: Treat the proxy as a privileged escape hatch and review its requests before use.

Risk: Cloud-control commands can modify or delete Flink resources.

Mitigation: Use a least-privilege RAM role in a test workspace and review each mutation, especially destructive actions.

Risk: SQL and configuration may expose secrets or be pushed to a Git repository.

Mitigation: Avoid embedding secrets in SQL and enable Git sync only for a repository approved to receive deployment artifacts.

Risk: Historical metrics require a user-supplied VVP Cookie.

Mitigation: Provide the Cookie only when historical metrics are needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-flink-sql-skill)
- [Flink SQL lifecycle](artifact/references/lifecycle.md)
- [Configuration and authentication](artifact/references/configuration.md)
- [CLI command reference](artifact/references/command-reference.md)
- [Git synchronization](artifact/references/git-sync.md)

## Skill Output:

**Output Type(s):** [Markdown, SQL code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with SQL and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational results depend on authenticated cloud access and read-back verification.]

## Skill Version(s):

0.0.1 (source: ClawHub release metadata and skill manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
