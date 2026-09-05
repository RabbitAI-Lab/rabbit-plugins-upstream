## Description:

Deploy an HTML page to the internet and return a public URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiantoucn](https://clawhub.ai/user/jiantoucn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to publish a local HTML page or supported site archive to Dropage and return a temporary public URL with optional expiry and visit limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected files may contain private data, credentials, or unpublished work and are uploaded to a public third-party service.

Mitigation: Review the file before upload and choose shorter expiry or visit limits when appropriate.

Risk: Long-expiry uploads can fail when per-IP or site-wide daily quotas are exhausted.

Mitigation: Report structured quota fields and reset times to the user, honor Retry-After, and avoid retry loops or silently changing the requested expiry.

## Reference(s):

- [Dropage deploy skill page](https://clawhub.ai/jiantoucn/skills/dropage-deploy)
- [Dropage deploy documentation](https://dropage.online/dropage-deploy.md)
- [Dropage upload API](https://dropage.online/api/upload)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a public URL, expiration time, and visit-limit status on successful upload.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
