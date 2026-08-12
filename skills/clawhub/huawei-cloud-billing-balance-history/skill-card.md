## Description:

Queries Huawei Cloud BSS account balance, balance change records, and monthly consumption summaries through read-only SDK calls and returns text or JSON reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Huawei Cloud billing status, including current balance, balance history over a date range, and monthly consumption summaries for cost review and debt monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing query inputs and results may be sent to a separate telemetry endpoint by default.

Mitigation: Use SKILL_QUALITY_DISABLE=1 unless outbound telemetry is explicitly approved, and treat billing outputs as sensitive account data.

Risk: The artifact includes real-looking billing and account data in test materials.

Mitigation: Redact account identifiers, balances, and test outputs before reuse or wider distribution.

Risk: Huawei Cloud AK/SK credentials can expose billing data if over-privileged or stored insecurely.

Mitigation: Use a least-privilege read-only billing key, keep credentials in environment variables, and avoid hardcoding secrets in files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-billing-balance-history)
- [IAM Policies](artifact/references/iam-policies.md)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Dataflow Diagram](artifact/references/dataflow-diagram.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON billing reports, with Markdown command examples and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud BSS queries; requires Huawei Cloud AK/SK credentials and Python SDK dependencies.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
