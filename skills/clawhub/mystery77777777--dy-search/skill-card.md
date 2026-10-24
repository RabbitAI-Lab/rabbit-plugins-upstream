## Description:

Searches Douyin videos by keyword and returns video details, engagement metrics, and optional CSV exports for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and analysts use this skill to collect public Douyin search results for topic research, competitor monitoring, and creator screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP service address can expose the service token in transit.

Mitigation: Use a verified HTTPS service address before logging in or sending a token.

Risk: The service token persists in a local configuration file.

Mitigation: Install only where local token storage is acceptable; protect the file and do not share or commit it.

Risk: Disabling HTTPS certificate checks increases interception risk.

Mitigation: Avoid insecure=true and use a backend with a valid certificate.

Risk: Submitting a collection task can deduct paid credits.

Mitigation: Require explicit user approval of the keyword, count, filters, and estimated cost before submitting.

## Reference(s):

- [dy-search ClawHub release](https://clawhub.ai/mystery77777777/skills/dy-search)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON responses and optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns video metadata and engagement counts, plus collected counts, charged credits, and refunds when available.]

## Skill Version(s):

1.0.0 (source: release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
