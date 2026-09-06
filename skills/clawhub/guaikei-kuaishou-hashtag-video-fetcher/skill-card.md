## Description:

Fetches public Kuaishou keyword search results, creator post lists, and video comments through Guaikei so agents can return structured JSON for content research, competitor monitoring, KOL discovery, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, analysts, and developers use this skill to collect public Kuaishou search, creator-post, and comment data for research workflows. Agents can run the Node.js commands when the user provides a keyword, profile URL, user ID, video URL, or video ID and a valid GUAIKEI_API_TOKEN is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou queries, target URLs, and GUAIKEI_API_TOKEN are sent to the Guaikei API.

Mitigation: Use only approved tokens and authorized research targets, and confirm that sending these inputs to Guaikei is allowed for the user's workflow.

Risk: Successful results are automatically saved under logs/ and may contain sensitive research records or personal data from public comments.

Mitigation: Protect the logs directory, avoid sharing saved result files unnecessarily, and delete logs when they are no longer needed.

Risk: The skill is limited to public Kuaishou data and may return empty or error statuses for missing, private, deleted, or inaccessible content.

Mitigation: Check the returned status and error_code before analysis, broaden narrow keywords when needed, and do not treat empty or error responses as successful findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-hashtag-video-fetcher)
- [Guaikei API Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful command results include status, error_code, message, timestamp, request metadata, skill metadata, and results; successful runs also save JSON results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29; artifact frontmatter metadata says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
