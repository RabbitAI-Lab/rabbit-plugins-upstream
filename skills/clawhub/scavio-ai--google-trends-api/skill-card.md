## Description:

Query Google Trends for interest-over-time, by-region, and related queries for a keyword, and pull real-time trending searches for a country as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Google Trends interest data, regional demand signals, related queries, and country-level real-time trending searches through Scavio. It supports market research, SEO, keyword research, and trend monitoring workflows that need structured JSON outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trend keywords, country queries, and related request parameters are sent to Scavio.

Mitigation: Use the skill only when sharing those query terms with Scavio is acceptable for the user's data handling requirements.

Risk: Endpoint calls consume Scavio credits and may fail when the account balance is exhausted.

Mitigation: Monitor credit usage and handle the documented 402 billing response before retrying.

Risk: Google Trends values are relative indices rather than absolute search counts.

Mitigation: Describe returned values as relative interest and avoid presenting them as absolute search volume.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-trends-api)
- [Scavio Google Trends documentation](https://scavio.dev/docs/google-trends)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response descriptions, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to call Scavio endpoints that return structured JSON trend data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
