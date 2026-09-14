## Description:

Searches Xiaohongshu public notes, retrieves note details and comments, and fetches public creator post lists for content research, competitor analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, brand marketers, analysts, and developers use this skill to collect structured public Xiaohongshu search results, note/comment details, and creator post lists for internal research, trend analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to the Guaikei third-party API and requires a GUAIKEI_API_TOKEN.

Mitigation: Install only if third-party API use is acceptable, keep the token scoped to this service, and avoid private or sensitive URLs.

Risk: Fetched Xiaohongshu public-data results can be saved locally in the logs directory.

Mitigation: Clean retained logs when research data is no longer needed and follow internal data-retention policies.

## Reference(s):

- [Xiaohongshu Tool on ClawHub](https://clawhub.ai/engheng-art/skills/xiaohongshu-tool)
- [Guaikei API service](https://www.guaikei.com)
- [Options and invocation reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: metadata.version, package.json, release.version, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
