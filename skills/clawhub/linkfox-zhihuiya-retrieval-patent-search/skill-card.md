## Description:

Searches the Zhihuiya (PatSnap) patent database with Analytics query expressions and returns matching patent records, publication numbers, key bibliographic fields, and hit counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, and developers use this skill to discover patents matching field-scoped Zhihuiya Analytics expressions, inspect the current result page, and decide whether to retrieve richer patent details with related skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries, selected session metadata, account onboarding data, and possible feedback text are sent to LinkFox services.

Mitigation: Use the skill only in a trusted workspace and avoid confidential searches unless external LinkFox processing is acceptable.

Risk: Full responses and cached query results may be stored locally as JSON files.

Mitigation: Review workspace data retention expectations before use and avoid sensitive queries if local saved JSON or cache files are not acceptable.

Risk: Onboarding can expose API keys in command output or configuration instructions.

Mitigation: Treat generated API keys as secrets and avoid sharing terminal output, logs, or saved configuration that contains them.

Risk: Custom LinkFox gateway environment variables can redirect requests to an unintended host.

Mitigation: Set LINKFOX_* gateway variables only to trusted LinkFox endpoints or leave the documented defaults in place.

Risk: Each patent search can consume account credits, and larger result pages cost more.

Mitigation: Start with a small limit, explain the credit impact before pagination or expanded searches, and do not automatically retry empty or failed searches with changed terms.

## Reference(s):

- [智慧芽-检索式专利检索 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-retrieval-patent-search)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown result tables and summaries, JSON response files, and shell commands for API or onboarding flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill writes full API responses to local JSON files, prints small responses inline, summarizes larger responses, and may cache matching query responses for 24 hours.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
