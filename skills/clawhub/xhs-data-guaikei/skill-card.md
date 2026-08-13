## Description:

Fetches public Xiaohongshu notes, note details, comments, and creator posts as structured data for topic research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and content operators use this skill to collect and analyze public Xiaohongshu content by keyword, note link, comment thread, or creator profile. It is not intended for login-gated, private, publishing, liking, or commenting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu links, keywords, filter choices, and retrieved public-content data to guaikei.com with a GUAIKEI_API_TOKEN.

Mitigation: Use it only when that third-party API transfer is acceptable for the task, and restrict inputs to public content within the user's authorization scope.

Risk: Xiaohongshu URLs may include xsec_token values that behave like sensitive shared links.

Mitigation: Treat those URLs as sensitive, avoid unnecessary sharing, and redact them from reports when the full URL is not required.

Risk: Searches, comments, and competitor research can remain in the local logs directory.

Mitigation: Periodically review and delete local logs when retained research data should not remain on disk.

Risk: The API token is required for all commands and could be misused if exposed.

Mitigation: Store GUAIKEI_API_TOKEN as an environment secret, avoid printing it in logs, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-data-guaikei)
- [Guaikei API token and support](https://www.guaikei.com)
- [Parameter and invocation guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and structured JSON results from executed commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0+; command results are saved to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
