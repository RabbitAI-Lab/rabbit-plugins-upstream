## Description:

鲸采云SRM is an OpenClaw skill that helps agents authenticate to Yidea SRM and manage supplier, procurement, inquiry, contract, order, receiving, payment, pricing, quota, material, and approval workflows through form-based CRUD operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yideamobileai](https://clawhub.ai/user/yideamobileai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and operations employees use this skill to submit, query, update, and review Yidea SRM records through natural-language requests. It covers supplier onboarding, purchase requests, quotations, contracts, purchase orders, receiving, payment, pricing, quotas, materials, and to-do approvals in an authenticated SRM environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide Yidea credentials in chat.

Mitigation: Install only in a trusted Yidea SRM environment, avoid shared workspaces, and treat entered credentials as sensitive.

Risk: The authentication flow writes a bearer token to config/config.json.

Mitigation: Restrict workspace access, remove or rotate the token after use, and avoid committing generated configuration files.

Risk: Broad natural-language triggers can lead to high-impact procurement actions such as create, update, delete, order, receipt, payment, or approval operations.

Mitigation: Require explicit human confirmation before executing any high-impact SRM change and review generated request parameters before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yideamobileai/skills/srm)
- [Server-resolved GitHub provenance](https://github.com/YideamobileAI/SRM)
- [Authentication guide](references/auth.md)
- [Global parameter protocol](references/protocol.md)
- [Standard business workflow](references/workflow.md)
- [Query field protocol](references/query-field.md)
- [Presentation guide](references/presentation.md)
- [Procurement form discovery](references/Procurement.md)
- [Relation table select handling](references/select-field/relation-table-mechanism.md)
- [Cascading select handling](references/select-field/cas-select-documentation.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with command examples, JSON request parameters, configuration updates, and formatted SRM query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include form schemas, CRUD operation arguments, approval/task summaries, and prompts for user confirmation before high-impact changes.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
