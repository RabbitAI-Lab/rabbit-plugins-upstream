## Description:

Retrieves public Xiaohongshu note, comment, profile-post, and engagement data through Guaikei so agents can support content research, KOL screening, competitor monitoring, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, analysts, and agent developers use this command skill to collect public Xiaohongshu search results, note details, creator posts, and comments for downstream analysis and reporting. It is intended for public-data lookup and does not support login, posting, engagement actions, private data access, or follower-count estimation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note/profile URLs, limits, and the GUAIKEI API token to guaikei.com.

Mitigation: Install and run it only when that third-party API use is acceptable for the intended data and authorization context.

Risk: Generated logs may retain research data, URLs with xsec_token parameters, comments, or business-sensitive content.

Mitigation: Treat the logs/ directory as retained research data and delete or protect it when it is no longer needed.

Risk: The skill returns public-data lookups that may be incomplete, empty, or unavailable due to token, URL, API, rate-limit, or network failures.

Mitigation: Check the command status and error_code fields, avoid treating empty/error results as successful data, and retry or correct inputs only when the reported failure mode supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-data)
- [Guaikei service website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [JSON from command-line scripts, with concise guidance for routing, inputs, failures, and follow-on analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package.json report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
