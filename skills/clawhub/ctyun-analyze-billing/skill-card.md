## Description:

Use when users ask to inspect, explain, reconcile, verify, or analyze CTYUN billing, charges, refunds, adjustments, product or resource costs, usage, billing-period changes, or dialogue billing reports through ctyun-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kqwjyk](https://clawhub.ai/user/kqwjyk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance reviewers use this skill to analyze CTYUN billing data through locally configured ctyun-cli commands, reconcile charges, and produce concise redacted billing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could expose sensitive account, order, transaction, resource, or billing details while analyzing bills.

Mitigation: Show only the smallest necessary redacted summary, avoid raw bill responses and long command transcripts, and do not store real bill data in tests, source control, caches, or external services.

Risk: Credential handling could leak CTYUN AccessKey or SecretKey values.

Mitigation: Use only the user's local ctyun-cli configuration; never run configure, request credentials, pass keys on the command line, or enable CLI logging.

Risk: Billing conclusions could be misleading when pagination, permissions, fields, or scope are incomplete.

Mitigation: Use bill API data as the source of truth, state query scope and source fields, complete pagination for full verification, and label incomplete results as partial data or cannot determine.

Risk: Troubleshooting or verification could expand beyond the user's approved billing scope.

Mitigation: Start with the smallest useful read-only bill query and require user approval before expanding account, project, product, region, resource, time, or verification scope.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/kqwjyk/skills/ctyun-analyze-billing)
- [CTYUN ctyun-cli installation guide](https://www.ctyun.cn/document/11095072/11096343)
- [Bill Actions and Runtime Discovery](references/bill-actions.md)
- [Bill Query Catalog](references/query-catalog.md)
- [Billing Evidence Policy](references/evidence-policy.md)
- [Dialogue Billing Report Specification](references/report-spec.md)
- [Billing Privacy Policy](references/privacy-policy.md)
- [Troubleshooting Without Guessing](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with redacted billing summaries and inline ctyun-cli commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should minimize sensitive billing data, avoid raw bill dumps, label evidence strength, and disclose partial coverage.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
