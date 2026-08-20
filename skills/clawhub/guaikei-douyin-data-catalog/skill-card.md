## Description:

Helps agents query Douyin public data for keyword search, creator posts, video comments, and hot-list tracking, while avoiding publishing, downloading, or private-data workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect structured Douyin public search results, creator posts, comments, and current hot-list data for content planning, competitor research, social listening, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad content-research requests that do not explicitly mention Douyin.

Mitigation: Narrow activation rules or require user confirmation before running Douyin data collection for generic research prompts.

Risk: Searches, creator data, and comments can be saved in local JSON logs.

Mitigation: Treat the logs directory as sensitive, restrict access, and delete retained logs when they are no longer needed.

Risk: Token and request details are sent to the Guaikei API.

Mitigation: Install only when this data flow is acceptable, keep GUAIKEI_API_TOKEN in environment configuration, and avoid exposing it in prompts or logs.

Risk: Runtime token-error behavior should be reviewed because the security summary reports a mismatch with the skill's safety claims.

Mitigation: Test invalid-token paths before deployment and block deployment if errors reveal contact, marketing, or sensitive token details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-catalog)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Complete option reference](references/options.md)
- [Release changelog](references/changelog.md)
- [JSON request and response schemas](assets/*.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON from command stdout with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN, sends requests to the Guaikei API, can return up to 10000 records per run, and writes local JSON logs by default.]

## Skill Version(s):

1.0.0 (source: release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
