## Description:

Routes Alibaba Cloud Dataphin administration requests to focused sub-skills for data planning, integration, development, operations, security, assets, data service APIs, knowledge graphs, and unstructured data workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Dataphin administrators use this skill suite to select and run the correct Dataphin workflow for tenant, project, data source, data development, operations, security, asset, API, knowledge graph, and unstructured data tasks. The skill is intended for governed administration where credentials, permissions, target environment, and write operations are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact Dataphin administration actions using powerful cloud credentials.

Mitigation: Install only in a Dataphin administration context and use a least-privilege, task-specific RAM identity.

Risk: Credential setup and API examples can expose secrets if copied into chat, shell history, logs, or command arguments.

Mitigation: Preconfigure credentials outside the session when possible and avoid placing AccessKey secrets or service credentials directly in command arguments.

Risk: Some workflows can write, delete, grant access, publish changes, update plugins, or modify local profiles.

Mitigation: Require human review before each write, delete, grant, publish, plugin update, or profile change.

Risk: Standalone Dataphin environments may be configured with certificate verification disabled.

Mitigation: Verify standalone certificates instead of disabling TLS verification whenever feasible.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [RAM Policies](references/ram-policies.md)
- [Related Commands](references/related-commands.md)
- [Version-Aware OpenAPI](references/version-aware-openapi.md)
- [OpenAPI Version Index](references/config/openapi-2.0-versions.json)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Alibaba Cloud CLI](https://github.com/aliyun/aliyun-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and occasional Python snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Dataphin CLI command plans, credential pre-check guidance, version-gated API routing, and validation steps.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
