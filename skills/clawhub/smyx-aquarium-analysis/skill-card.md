## Description:

Analyzes aquarium pet images, videos, or media URLs through a remote service to produce structured fish health findings, possible disease indicators, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit aquarium pet media for fish and aquatic pet health analysis, including scale, fin, color, activity, and common disease indicators. It can also return cloud-stored historical report lists associated with the local skill identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media files or URLs are sent to remote lifeemergence.com services for analysis.

Mitigation: Use only media approved for third-party processing, and avoid private videos, sensitive account contexts, or internal URLs unless the service terms and retention behavior are acceptable.

Risk: The skill creates or reuses an internal local user identity, logs into the remote service, and stores returned tokens in a workspace SQLite database.

Mitigation: Run the skill in an isolated workspace, restrict workspace access, and remove the local data store or tokens after use when the account context is sensitive.

Risk: The skill can query cloud report history associated with the local identity.

Mitigation: Confirm that report-history access is appropriate for the workspace and ask the publisher for clearer consent, retention, and token-deletion controls before production use.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [smyx_analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown or plain text containing structured JSON analysis, report summaries, health guidance, and report links; optional output files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis depends on remote lifeemergence.com services, supports local files or media URLs, and can query cloud report history.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence; artifact frontmatter differs: 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
