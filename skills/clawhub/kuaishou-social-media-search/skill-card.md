## Description:

Searches public Kuaishou videos by keyword, retrieves public creator posts and video comments, and returns structured results for social-media analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, and analysts use the skill to examine public Kuaishou videos, creator activity, and comments for topic research, competitor monitoring, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, video or profile URLs, and the API token are sent to the third-party Guaikei service.

Mitigation: Confirm third-party sharing is acceptable before use; avoid submitting sensitive inputs and protect the token.

Risk: Fetched public results, including comments and usernames, are saved in the local logs directory.

Mitigation: Restrict access to logs and delete saved results when no longer needed.

## Reference(s):

- [Option and usage reference](references/options.md)
- [Release changelog](references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Analysis, JSON]

**Output Format:** [Structured JSON results with optional plain-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include success, empty, or error status; fetched results are also saved locally in logs/.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
