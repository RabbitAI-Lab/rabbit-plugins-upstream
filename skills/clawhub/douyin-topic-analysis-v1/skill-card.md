## Description:

Provides command-line access to public Douyin search, hot-list, creator-post, and comment data for topic research, competitor monitoring, social listening, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content operators, brand researchers, creators, and developers use this skill to retrieve structured public Douyin data for short-video topic selection, competitor monitoring, trend tracking, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Guaikei API token and Douyin query targets are sent to www.guaikei.com, and the security review notes that the token is passed in URL query strings.

Mitigation: Use the skill only after accepting that third-party data flow, keep the token out of shared terminals and logs, and rotate the token immediately if it may have been exposed.

Risk: Search, post, and comment outputs may be saved under the local logs directory and can include sensitive research targets or public personal data such as usernames and comments.

Mitigation: Review retained logs, delete datasets that are no longer needed, and redact personal or sensitive fields before sharing analysis outside the authorized team.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/douyin-topic-analysis-v1)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-topic-analysis-v1)
- [Guaikei Douyin data API](https://www.guaikei.com)
- [Complete options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with command examples and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands write JSON to stdout, send logs to stderr, and may save fetched datasets under a local logs directory.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
