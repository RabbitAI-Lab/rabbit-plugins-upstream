## Description:

Collects public Kuaishou keyword search results, creator posts, and video comments through CLI commands and returns structured JSON for content analysis, competitor monitoring, KOL discovery, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, MCN teams, and data analysts use this skill to retrieve public Kuaishou video, creator, and comment data for topic research, competitor monitoring, KOL screening, sentiment review, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, and request parameters are sent to the GUAIKEI third-party API.

Mitigation: Use the skill only for public, non-sensitive investigations and confirm that the user is comfortable with third-party API processing before execution.

Risk: Returned public-data results may be stored in the skill's local logs directory.

Mitigation: Delete local logs when they are no longer needed and avoid collecting private, login-only, or sensitive investigation data.

Risk: The skill requires a GUAIKEI_API_TOKEN to call the third-party API.

Mitigation: Provide the token through the environment, keep it out of prompts and committed files, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/kuai-shou-ai-feed)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON results with status, request metadata, and returned public-data records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs may also save returned results under a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and references/changelog.md; artifact package/frontmatter list 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
