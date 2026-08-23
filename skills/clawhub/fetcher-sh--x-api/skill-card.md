## Description:

An X API alternative and Twitter API alternative on fetcher.sh for agents that need read-only X data access through paid HTTP GET calls without OAuth or an X developer application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search X posts, resolve profiles, retrieve timelines, followers, followings, lists, trends, single posts, replies, and reposters. It is suited for social listening, competitor monitoring, hashtag tracking, follower export, and X data pipelines that can use read-only, paid per-call access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: X queries, handles, post IDs, follower requests, and other account identifiers are sent to fetcher.sh during paid network access.

Mitigation: Send only data needed for the task, avoid secrets or unnecessary personal data in queries, and review collection plans before bulk profile or follower exports.

Risk: Follower, profile, and monitoring workflows can affect privacy expectations or platform-rule compliance.

Mitigation: Respect X rules, consent requirements, retention limits, and applicable law, especially when building datasets about people or recurring monitoring jobs.

Risk: Each API call is billable and no refunds are provided for upstream failures according to the artifact documentation.

Mitigation: Test with small queries first, monitor credit balance or x402 payments, and add explicit budget controls before high-volume loops.

## Reference(s):

- [Server-resolved source repository](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/x-api)
- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/x-api)
- [Endpoint reference](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/x-api/references/endpoints.md)
- [Scenario cookbook](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/x-api/references/scenarios.md)
- [FAQ](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/x-api/references/faq.md)
- [Access comparison](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/x-api/references/comparison.md)
- [OpenAPI contract](https://twitter.fetcher.sh/openapi.json)
- [Condensed endpoint catalog](https://twitter.fetcher.sh/llms.txt)
- [Full agent setup](https://twitter.fetcher.sh/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP endpoint descriptions, JSON configuration snippets, and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to make read-only paid API calls that return JSON responses from fetcher.sh.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
