## Description:

Neural web search, parsed page contents, find-similar, and agentic Q&A over the live web through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the live web, retrieve parsed page contents, find semantically similar URLs, and produce sourced answers through a connected Superagnt/Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, URLs, and content-fetch requests are sent to Superagnt/Exa.

Mitigation: Avoid sending secrets or regulated data unless approved for the connected Superagnt/Exa workflow.

Risk: Vendor-side rate limits or billing may apply to the connected Exa account.

Mitigation: Confirm account limits and billing expectations before high-volume use.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/exa-search)
- [Superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, SUPERAGNT_API_KEY, and a connected Exa account. Search terms, URLs, and content-fetch requests are sent to Superagnt/Exa.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
