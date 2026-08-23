## Description:

Helps agents retrieve public Douyin search results, creator posts, video comments, and hot-list data for competitor monitoring, content research, public-opinion analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public Douyin content, creator posts, comments, and trending topics through Node.js CLI tools that return structured JSON for competitive analysis, marketing research, and monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, URLs, and returned public data may be processed by the external guaikei.com service.

Mitigation: Use only data appropriate for external processing, avoid private or sensitive inputs, and review the service behavior before operational use.

Risk: Collected public data is saved in local log files by default.

Mitigation: Review, protect, and rotate the logs directory, and delete outputs that are no longer needed.

Risk: The GUAIKEI_API_TOKEN functions as a credential.

Mitigation: Store the token only in an environment variable, avoid printing or committing it, and rotate it if exposure is suspected.

Risk: Runtime token-error behavior conflicts with the skill's stated no-promotion rule.

Mitigation: Review authentication error output before deployment and ensure users are not shown unintended contact, website, or payment-promotion text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/douyin-competitor-watch-guaikei)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [CLI JSON schemas](assets/*.schema.json)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI tools emit JSON to stdout and write JSON log files locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and a GUAIKEI_API_TOKEN environment variable; queries and returned public Douyin data may be processed by guaikei.com and saved in logs by default.]

## Skill Version(s):

1.0.0 (source: package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
