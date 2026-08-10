## Description:

Guaikei XHS Tool helps agents retrieve public Xiaohongshu keyword search results, note details, comments, and creator post lists as structured JSON through the Guaikei API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, and data analysts use this skill to collect public Xiaohongshu data for content research, trend monitoring, competitor analysis, KOL screening, and comment analysis. The skill requires a GUAIKEI_API_TOKEN and is limited to public, non-private data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, requested limits, and GUAIKEI_API_TOKEN are sent to the Guaikei API service.

Mitigation: Use the skill only when that third-party data transfer is acceptable, avoid sensitive search terms, and manage the token as a secret.

Risk: Command results are saved locally by default and may contain collected public content or research queries.

Mitigation: Review the generated logs directory periodically and delete records that should not remain on shared or long-lived systems.

Risk: The skill is limited to public Xiaohongshu data and may return empty or error responses for private, deleted, unavailable, or rate-limited content.

Mitigation: Validate input links and keywords, handle status and error_code fields before analysis, and do not treat empty results as confirmed findings.

## Reference(s):

- [Options and CLI usage](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results are saved locally to a logs directory by default; API calls require GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
