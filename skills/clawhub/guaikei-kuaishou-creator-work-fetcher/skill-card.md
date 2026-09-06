## Description:

Fetches public Kuaishou/Kwai video search results, creator public works, and video comments for content research, creator monitoring, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketing teams, and data analysts use this skill to retrieve public Kuaishou data for keyword research, competitor monitoring, creator work review, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, profile or video URLs, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Install and run only when the user accepts this data sharing path, and avoid submitting sensitive research terms or links beyond the intended public-data task.

Risk: Collected result payloads are saved locally under the skill's logs directory.

Mitigation: Review or delete generated logs after sensitive research tasks, especially when collecting large creator or comment datasets.

Risk: The skill is intended for public Kuaishou data and does not support private, hidden, login-required, or interactive account actions.

Mitigation: Use it only for public-data retrieval and reject requests for private content, account login, posting, likes, follows, or other user interactions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-creator-work-fetcher)
- [Guaikei API access and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON status, request metadata, and result payloads, with local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14+ and GUAIKEI_API_TOKEN; supported commands fetch keyword search results, creator public works, or video comments.]

## Skill Version(s):

1.0.0 (source: server release metadata, skill frontmatter, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
