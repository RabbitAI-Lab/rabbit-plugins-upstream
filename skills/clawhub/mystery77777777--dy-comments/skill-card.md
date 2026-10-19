## Description:

Collects public Douyin video comments and replies in user-approved steps, with JSON results and CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and other users collect comments and replies from public Douyin videos for sentiment or audience research, reviewing results one paid step at a time and exporting collected data to CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login tokens and requests may cross the network without encryption under the default HTTP service URL.

Mitigation: Confirm that you trust the service and account model; switch to a verified HTTPS endpoint before login when available.

Risk: Disabling TLS certificate verification can expose credentials and collected data to interception.

Mitigation: Keep insecure TLS mode disabled and use an endpoint with a valid certificate.

Risk: Older credentials may be imported automatically from ~/.xhs-convert.

Mitigation: Check for and review any existing credentials before running the CLI; use an isolated configuration path if appropriate.

Risk: Each comment-page collection or reply expansion can spend account credits.

Mitigation: Show the estimate first and obtain explicit approval before each paid collection step or expansion.

Risk: Exported comments can contain public nicknames and location information.

Mitigation: Limit collection to authorized or public-data research and safeguard exported CSV files.

## Reference(s):

- [dy-comments on ClawHub](https://clawhub.ai/mystery77777777/skills/dy-comments)

## Skill Output:

**Output Type(s):** [Text, CSV files, Guidance]

**Output Format:** [JSON command responses, CSV export, and conversational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incremental comment batches and replies; exported CSV includes comment details.]

## Skill Version(s):

1.0.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
