## Description: <br>
AssetClaw helps agents operate AssetHub asset lifecycle workflows, including asset lookup, repair and maintenance work orders, allocation approvals, inventory, depreciation, procurement, scrapping, quality records, documentation, spare parts, labeling, alerts, IoT monitoring, compliance, and related API-backed tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmu4hlee](https://clawhub.ai/user/cmu4hlee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AssetHub operators and implementation teams use this skill to query, create, update, approve, and audit asset-management records through the AssetHub API. It is suited to trusted operational environments where agents need guided access to asset, maintenance, procurement, inventory, compliance, IoT, and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad AssetHub API coverage, including administrative and high-risk write operations. <br>
Mitigation: Install only for trusted AssetHub operators, restrict accounts with server-side RBAC, and require explicit human approval for backup, system-config, service-token, tenant, role, wx-cloud, destructive, or cross-tenant actions. <br>
Risk: Login credentials and session tokens may be stored in local temporary session files during operation. <br>
Mitigation: Avoid entering real passwords into prompts, prefer short-lived tokens or a protected secret store, use limited-privilege accounts, and clear sessions after use. <br>
Risk: API calls can affect live AssetHub data when pointed at a remote or production API target. <br>
Mitigation: Use HTTPS or localhost-only API targets, verify the configured API URL before execution, and test write workflows in a controlled tenant before production use. <br>
Risk: High-risk actions can require idempotency keys and a second confirmation token. <br>
Mitigation: Use stable idempotency keys for retries, keep automatic high-risk replay disabled unless a human explicitly confirms, and stop automation if confirmation still fails. <br>


## Reference(s): <br>
- [AssetClaw ClawHub skill page](https://clawhub.ai/cmu4hlee/skills/assetclaw) <br>
- [AssetHub website](http://www.medfix.cn) <br>
- [Authentication and workflows](references/auth-and-workflows.md) <br>
- [API conventions](references/api-conventions.md) <br>
- [API modules overview](references/api-modules-overview.md) <br>
- [Endpoint quick reference](references/endpoint-quick-ref.md) <br>
- [API domain map](references/api-domain-map.md) <br>
- [Route mount map](references/route-mount-map.md) <br>
- [Middleware reference](references/middleware.md) <br>
- [Asset state machine](references/asset-state-machine.md) <br>
- [API catalog snapshot](references/api-catalog-2026-07-29.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and API operation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AssetHub API requests, environment-variable configuration, tenant-context guidance, and operational cautions for high-risk actions.] <br>

## Skill Version(s): <br>
1.7.0 (source: ClawHub release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
