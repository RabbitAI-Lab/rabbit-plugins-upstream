## Description:

Identifies bird species in target-area images or videos, supports at least 500 common species, and can return structured reports for ecological observation and birdwatching scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify bird species from local images, videos, or public media URLs, retrieve structured analysis reports, and query prior cloud reports associated with the current internal user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bird images, videos, or media URLs are sent to a third-party cloud service for analysis.

Mitigation: Use only media that is appropriate for third-party processing, avoid sensitive locations or bystanders, and confirm organizational approval before upload.

Risk: The skill automatically associates requests with an internal user identity and can query cloud history.

Mitigation: Make identity association and history lookup explicit to administrators and users before deployment, and avoid environments where silent account creation or history access is not allowed.

Risk: Returned authentication tokens may be stored in a local workspace SQLite database.

Mitigation: Restrict workspace file access, avoid sharing the workspace, and rotate or revoke tokens if the workspace may have been exposed.

Risk: The authoritative scan verdict is suspicious because the API client has broader account and history behavior than the bird-recognition description suggests.

Mitigation: Review the API permissions and endpoints before use, and prefer a release that clearly declares permissions and scopes the client to bird-recognition functions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Bird recognition API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files]

**Output Format:** [Markdown text or JSON structured report, with optional saved output file and report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video file input, public media URL input, history-list queries, and optional output file path; documented size limit is 10 MB.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
