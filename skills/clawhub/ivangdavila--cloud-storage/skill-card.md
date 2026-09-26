## Description:

Manage files across cloud providers with authentication, cost awareness, and multi-provider operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers, engineers, and agents use this skill to upload, download, sync, and manage files across object storage and consumer cloud storage providers while accounting for authentication, rate limits, verification, and cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials, service account keys, client secrets, SAS tokens, and OAuth refresh tokens can expose storage resources if mishandled.

Mitigation: Use least-privilege accounts, prefer managed or keyless identity where supported, avoid root or broad keys, and store tokens as sensitive secrets.

Risk: Large transfers or repeated listing operations can produce unexpected egress, API, and storage charges.

Mitigation: Estimate transfer, storage, and operation costs before bulk work and verify current provider pricing before execution.

Risk: Deletion or migration tasks can lose data if success is assumed from API responses or backups are not restorable.

Mitigation: Verify object existence, size or checksums, and backup restorability before deleting source data.

## Reference(s):

- [Cloud Storage skill page](https://clawhub.ai/ivangdavila/skills/cloud-storage)
- [Provider-specific patterns](artifact/providers.md)
- [Authentication setup](artifact/auth.md)
- [Cost calculation](artifact/costs.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Code]

**Output Format:** [Markdown guidance with tables, checklists, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only cloud storage helper; no hidden execution behavior reported by security evidence.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
