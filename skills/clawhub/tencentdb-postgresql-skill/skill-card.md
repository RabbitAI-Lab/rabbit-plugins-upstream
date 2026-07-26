## Description: <br>
Bundle entry for TencentDB PostgreSQL skills that routes Tencent Cloud PostgreSQL management, mem0 and REST extension-service, inspection, and slow SQL requests to focused sub-scenarios while preserving explicit safety boundaries for ambiguous targets and high-risk changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database operators use this skill to inspect TencentDB for PostgreSQL instances, route management-plane requests, query slow SQL, and operate mem0 or REST extension-service workflows with target and confirmation checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Tencent Cloud PostgreSQL settings when credentials and a target are available. <br>
Mitigation: Use a least-privilege CAM subaccount, avoid long-lived high-privilege keys, and provide only the exact region and instance ID needed for the task. <br>
Risk: Cloud credentials or temporary tokens could be exposed if pasted into chat or stored in source files. <br>
Mitigation: Place Tencent Cloud credentials only in the host runtime environment and do not paste SecretKey, API keys, or session tokens into chat, URLs, repository files, or query parameters. <br>
Risk: Opening, closing, or modifying services can affect availability, network exposure, or cost. <br>
Mitigation: Require explicit user confirmation for write, fee-impacting, or high-risk actions after reporting the affected instance, intended operation, and safety implications. <br>
Risk: Ambiguous regions or instance identifiers can direct actions at the wrong database instance. <br>
Mitigation: Normalize regions, stop when the target cannot be narrowed safely, and ask for a standard region plus a PostgreSQL instance ID before executing target-specific operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tencent-adm/skills/tencentdb-postgresql-skill) <br>
- [TencentDB PostgreSQL Skill Source](artifact/SKILL.md) <br>
- [Management-plane Router Reference](artifact/references/tencent-pg-management/references/api_reference.md) <br>
- [mem0 Service Control Reference](artifact/references/tencent-pg-mem0-deploy/references/api_reference.md) <br>
- [REST Service Control and Troubleshooting Reference](artifact/references/tencent-pg-rest-deploy/references/api_reference.md) <br>
- [Inspection Monitor Reference](artifact/references/tencent-pg-inspection/references/api_reference.md) <br>
- [Slow Query Lookup Reference](artifact/references/tencent-pg-slowquery-diagnosis/references/api_reference.md) <br>
- [Common Error Handling Rules](artifact/references/common/error_handling.md) <br>
- [Tencent Cloud PostgreSQL Console](https://console.cloud.tencent.com/postgres) <br>
- [Tencent Cloud API Key Management](https://console.cloud.tencent.com/cam/capi) <br>
- [Tencent Cloud PostgreSQL API Endpoint](https://postgres.tencentcloudapi.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured result sections and inline shell or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include target scope, current facts, task IDs, HTTP status summaries, risk review notes, and safe next steps.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
