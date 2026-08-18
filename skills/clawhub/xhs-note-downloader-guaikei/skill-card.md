## Description:

Retrieves public Xiaohongshu note details, comments, keyword search results, and creator posts so an agent can support KOL screening, trend analysis, competitor monitoring, and content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to retrieve public Xiaohongshu content and interaction data for content ideation, comment analysis, KOL review, and competitor monitoring. It requires a GUAIKEI_API_TOKEN and sends user-provided Xiaohongshu keywords or URLs to guaikei.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Xiaohongshu keywords, note/profile URLs, request metadata, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that data sharing is approved, and avoid submitting sensitive or unnecessary queries and URLs.

Risk: Returned comments and creator data can be public-but-sensitive and may be retained locally in logs/.

Mitigation: Use the smallest practical --limit value, restrict access to generated result files, and clean logs/ when results should not be retained.

Risk: Missing, invalid, or rate-limited API tokens can cause empty or failed retrievals.

Mitigation: Confirm GUAIKEI_API_TOKEN is configured before use, handle error or empty status values explicitly, and do not fabricate conclusions from failed retrievals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-note-downloader-guaikei)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON objects on stdout, with command guidance and optional downstream prose or Markdown summaries from the calling agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save returned task results as JSON files under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package metadata report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
