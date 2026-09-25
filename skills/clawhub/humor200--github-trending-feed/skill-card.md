## Description:

Fetches public GitHub Trending repositories, enriches them with GitHub repository metadata, and returns structured JSON for an agent to format for chat, feed, or console delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[humor200](https://clawhub.ai/user/humor200)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to retrieve current GitHub Trending repository data and publish concise repository summaries in chat, feed, or console workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound requests to GitHub, so use depends on GitHub availability, rate limits, and acceptable external network access.

Mitigation: Install only in environments where outbound GitHub access is acceptable, and use caching or rate limiting for frequent polling.

Risk: The advertised language filter appears broken, so filtered requests may return default Trending results.

Mitigation: Verify repository languages before publishing filtered feeds, or fix the filter implementation before relying on it.

Risk: When live fetching fails, fallback repository data can be stale or incomplete.

Mitigation: Surface fetch errors to downstream agents and avoid presenting fallback output as a verified current trend list.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/humor200/skills/github-trending-feed)
- [GitHub Trending](https://github.com/trending)

## Skill Output:

**Output Type(s):** [json, guidance]

**Output Format:** [JSON array of repository objects, with optional text or markdown formatting by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is about 9 to 10 repositories; each item can include full_name, description, language, stars, url, and error.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
