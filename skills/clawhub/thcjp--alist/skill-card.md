## Description:

AList provides unified cloud-drive management for uploading, downloading, sharing, deleting, and tracking files across AList-backed storage providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage AList-backed cloud drives, create protected share links, and support virtual-product delivery workflows with link tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload, share, delete, and retrieve cloud-drive content through the configured AList MCP server.

Mitigation: Review MCP server permissions, use a limited AList account where possible, and require confirmation before uploads, deletions, downloads, or share-link creation.

Risk: The skill can create delivery links and track customer delivery data.

Mitigation: Apply retention rules for delivery records and require confirmation before customer-facing delivery or redelivery actions.

Risk: The skill depends on AList credentials and endpoint configuration.

Mitigation: Store ALIST_BASE_URL, ALIST_USERNAME, and ALIST_PASSWORD in the agent environment or secret manager and avoid exposing them in prompts, logs, or generated output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/alist)

## Skill Output:

**Output Type(s):** [text, JSON, configuration, guidance]

**Output Format:** [JSON responses and concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include share URLs, passwords, expiry timestamps, file metadata, download URLs, delivery status, and error codes.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
