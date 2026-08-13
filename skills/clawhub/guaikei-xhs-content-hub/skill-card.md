## Description:

This skill helps agents search public Xiaohongshu notes, retrieve note details and comments, and collect creator posts for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, data analysts, and agent operators use this skill to collect and summarize public Xiaohongshu content, comments, and creator activity for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and the Guaikei API token are sent to the Guaikei service.

Mitigation: Use the skill only when third-party API processing is acceptable, avoid private or sensitive links, and keep GUAIKEI_API_TOKEN scoped and rotated according to local policy.

Risk: Successful results may be saved locally under logs/.

Mitigation: Periodically delete saved logs and avoid running the skill in shared workspaces when the research topic or returned data is sensitive.

Risk: Requests for private, hidden, login-only, or publishing actions are outside the skill's supported behavior.

Mitigation: Restrict use to public Xiaohongshu data collection and decline tasks that require private content, authentication state, posting, liking, or commenting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-content-hub)
- [Guaikei service website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and structured JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
