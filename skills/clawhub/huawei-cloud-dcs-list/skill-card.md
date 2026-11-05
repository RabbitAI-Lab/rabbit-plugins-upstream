## Description:

Lists Huawei Cloud DCS (Redis or Memcached) instances in a tenant region through KooCLI or the Huawei Cloud SDK fallback, with filters and name, table, or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect tenant DCS inventory, review instance status, and retrieve instance IDs before related operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exact-name matching ignores tag filters, so combining --name-equal with --tags can return instances outside the requested tag filter.

Mitigation: Until a corrected version preserves tag filters, avoid combining --name-equal with --tags.

Risk: DCS_LIST_HCLOUD_* environment overrides can bypass the promised read-only command behavior.

Mitigation: Clear all DCS_LIST_HCLOUD_* overrides and use a trusted CLI with a dedicated read-only account.

Risk: Live cloud behavior and downloaded installer contents were not verified in the offline review.

Mitigation: Use a trusted CLI installation and a dedicated read-only account; treat live behavior as unverified until checked in the target environment.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [KooCLI Installation Guide](references/cli-installation-guide.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Least-Privilege IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Instance names or a full-field table as text, or the raw instance array as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact instance names by default; optional full-field table or JSON array, with automatic pagination.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
