## Description:

Use when scripting or batch-driving a NetBox instance over the REST API for device relocation, renaming, cabling, IP assignment, and pre-verify/read-back workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[indane](https://clawhub.ai/user/indane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to plan and execute NetBox REST API operations such as moving devices, updating rack positions, assigning IPs, and validating batch changes with read-back checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to use a stored NetBox token for live infrastructure inventory changes.

Mitigation: Use a least-privilege NetBox token, review planned writes before execution, pre-verify object IDs against fresh GET results, and read back after every batch.

Risk: TLS certificate verification can be disabled with NETBOX_INSECURE_TLS.

Mitigation: Keep certificate verification enabled by default and use NETBOX_INSECURE_TLS only for controlled internal networks or self-signed CA scenarios where the operator understands the risk.

Risk: Incorrect NetBox field names or stale object IDs can produce no-op or unintended updates.

Mitigation: Build plans from fresh API reads, match objects by expected names, abort on mismatches, and compare post-write state against the source plan.

## Reference(s):

- [NetBox REST API quick reference](references/netbox-api.md)
- [Batch device operations verified recipe](references/batch-device-operations.md)
- [ClawHub release page](https://clawhub.ai/indane/skills/netbox-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON payloads, shell command snippets, and Python CLI usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include NetBox REST API paths, PATCH payloads, pagination guidance, token-handling guidance, and read-back verification steps.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
