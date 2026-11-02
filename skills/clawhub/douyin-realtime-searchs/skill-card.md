## Description:

Searches current public Douyin videos and posts, hot lists, creator works, and comments by keyword or link, with filters for ranking, time, duration, and content type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, analysts, and marketing teams use the skill to find current public Douyin content, monitor hot topics, review creator activity, and summarize public comment trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and links are sent to a third-party provider, and requests may incur provider charges.

Mitigation: Use only when that data transfer is acceptable, keep requests scoped to public Douyin data, and check provider charges before large queries.

Risk: The provider API token and locally saved result logs may expose sensitive information if mishandled.

Mitigation: Protect the API token and delete saved logs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-realtime-searchs)
- [Guaikei provider website](https://www.guaikei.com)
- [Command options](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON result envelopes containing public Douyin search, hot-list, creator, or comment data; the agent can summarize results in text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be empty or include errors; media and share links can expire.]

## Skill Version(s):

1.4.0 (source: server release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
