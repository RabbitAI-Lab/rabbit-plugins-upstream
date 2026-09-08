## Description:

Retrieves company filings and XBRL facts, then produces cited, non-advisory risk analyses and investment research reports from platform-backed source tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to query public company filing data, inspect XBRL facts, and generate research reports with citations, timestamps, risk notes, and a clear non-advice disclaimer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake generated research reports or risk analyses for personalized financial advice or trading instructions.

Mitigation: Keep outputs informational, preserve the non-advice disclaimer, and refuse requests for guaranteed returns, buy/sell/hold instructions, target prices, or trade timing.

Risk: API keys could be exposed if pasted into request bodies, logs, references, or reports.

Mitigation: Store INVESTMENT_RESEARCH_API_KEY only as an environment variable and do not include secrets in JSON payloads, logs, citations, or generated reports.

Risk: Changing AI_SKILLS_API_URL can route requests to an endpoint the user did not intend to trust.

Mitigation: Use the default AI Skills platform URL unless the user has intentionally selected and trusts a different endpoint.

Risk: Reports can become misleading if source_task_ids are fabricated, stale, failed, or taken from unrelated tasks.

Mitigation: Use only real succeeded or evidenced partial source task IDs from the current user and product, and preserve accession, form, filed date, period, unit, source, and observed_at details for each conclusion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/investment-research)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [Source Evidence and Investment Safety Rules](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown and JSON-oriented API responses with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires INVESTMENT_RESEARCH_API_KEY; reports include citations, timestamps, risk notes, and a non-advice disclaimer.]

## Skill Version(s):

1.5.0 (source: server release metadata and frontmatter packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
