## Description:

Investment Research helps agents retrieve company filings and XBRL facts, then create cited risk analyses or investment research reports without investment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query public filing data through the AI Skills platform and produce cited, non-advisory risk analysis or research reports from verified source task IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a product-specific API key and may involve usage billing.

Mitigation: Install it only when the AI Skills platform is trusted for the key, keep the key out of logs and reports, and review billing information returned by the platform.

Risk: Investment research outputs could be mistaken for personalized financial advice or trading instructions.

Mitigation: Use outputs only as cited informational research; preserve the non-advisory disclaimer and do not use the skill for automated trading, order execution, guaranteed returns, or buy, sell, or hold instructions.

Risk: Reports can become misleading if they are built from invalid, stale, unauthorized, failed, or fabricated source task IDs.

Mitigation: Create risk analyses and reports only from current, authorized platform tasks that succeeded or returned evidenced partial results, and keep accession, filing date, period, source, and observed-at metadata with conclusions.

Risk: Provider failures, partial results, or empty results may be overinterpreted.

Mitigation: Report missing or partial data as a limitation of the returned sources and avoid treating empty results as proof that a fact does not exist.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [Sources, Evidence, and Investment Safety Rules](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces cited, non-advisory filing research outputs from verified platform task IDs.]

## Skill Version(s):

1.4.1 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
