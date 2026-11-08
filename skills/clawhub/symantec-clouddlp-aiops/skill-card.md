## Description:

Use for read-only Symantec Cloud DLP incidents, profiles, detection content, custom groups, data identifiers, and index health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Security and DLP administrators use this skill to inspect Cloud DLP incidents, profiles, detection content, custom groups, data identifiers, and index health through read-only operations. Use bounded incident searches and treat missing, partial, or unverified responses as unknown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed package implementation and its linked operations and verification documents are not included for review, so its behavior and live-environment coverage are not fully verified.

Mitigation: Review the installed package before granting access to sensitive DLP data; use read-only credentials and bounded searches, and interpret missing or incomplete results as unknown.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/symantec-clouddlp-aiops)
- [Declared project homepage](https://github.com/AIops-tools/Symantec-CloudDLP-AIops)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text summaries and surfaced API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query results; raw profile response shapes may be surfaced.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
