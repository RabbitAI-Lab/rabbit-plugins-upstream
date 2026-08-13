## Description:

CordysCRM helps CRM users work across the lead-to-cash lifecycle with cross-module tracing, funnel analysis, Customer 360 views, workflow guidance, and CLI-backed Cordys CRM operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fit2-zhao](https://clawhub.ai/user/fit2-zhao)

### License/Terms of Use:

MIT-0

## Use Case:

CRM, sales, finance, contract, and executive users use this skill to query and update Cordys CRM records, inspect lead-to-cash status, review approvals, and receive role-specific risk warnings and next-action guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use CRM credentials for broad raw API calls and high-impact approval, financial, and account changes.

Mitigation: Install only for trusted publishers, provide least-privilege Cordys CRM credentials, and require review before approval-flow, financial write, or account-changing actions are used with production data.

Risk: Untrusted CRM domains or unrestricted raw API calls could expose credentials or send requests to unintended endpoints.

Mitigation: Use only trusted CORDYS_CRM_DOMAIN values, avoid enabling CORDYS_ALLOW_UNTRUSTED, and avoid raw API calls unless the endpoint and payload have been reviewed.

Risk: Local role persistence can influence the scope of CRM queries and actions across sessions.

Mitigation: Review user-role.md persistence behavior before production use and confirm role mappings match the intended user permissions.

## Reference(s):

- [Cordys CRM API Reference](artifact/references/crm-api.md)
- [CLI Semantic Specification](artifact/core/cli-spec.md)
- [Write Operation Engine](artifact/core/write-engine.md)
- [Risk Identification Engine](artifact/core/risk-engine.md)
- [ClawHub Skill Page](https://clawhub.ai/fit2-zhao/skills/cordys-crm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CRM summaries, tables, warnings, recommendations, and inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses role-specific CRM views and limits large result displays to concise summaries.]

## Skill Version(s):

1.2.1 (source: server release metadata and artifact registry)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
