## Description:

This skill helps agents query public Douyin data through guaikei, including keyword search, creator post retrieval, video comment collection, and real-time hot list lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and structure public Douyin search results, creator posts, video comments, and hot-list data for content research, competitor analysis, public-opinion review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send broad Douyin research requests to a third-party API.

Mitigation: Use it only when Douyin is the intended platform and keep requests scoped to the user's stated research need.

Risk: Fetched public profile and comment data can be saved to local logs.

Mitigation: Treat logs as retained data, delete them when no longer needed, and avoid redistributing collected personal or comment data outside the allowed use case.

Risk: The guaikei API token is required for execution.

Mitigation: Store GUAIKEI_API_TOKEN only in the environment, avoid printing or sharing it, and rotate it if exposed.

## Reference(s):

- [guaikei data service](https://www.guaikei.com)
- [Command options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses from Node.js CLI commands, with optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0 or newer; results may include public profile or comment data and should be handled as retained data when logs are written.]

## Skill Version(s):

1.0.0 (source: server metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
