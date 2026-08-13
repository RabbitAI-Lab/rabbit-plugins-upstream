## Description:

Searches the Zhihuiya (PatSnap) patent database with Analytics query expressions and returns matching patent IDs, publication numbers, basic patent fields, hit counts, and cost data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, IP analysts, and developers use this skill to discover patents with Zhihuiya Analytics expressions, inspect paged search results, and decide whether to fetch detailed records with related skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search queries, search results, API keys, payment links, and order metadata may be sensitive.

Mitigation: Use a dedicated scoped API key where possible, avoid sharing generated linkfox files or stdout logs, and treat payment and order artifacts as sensitive.

Risk: The skill sends patent searches and account or billing actions through LinkFox/Zhihuiya services.

Mitigation: Install and run it only when those services are acceptable for the intended data and workflow.

Risk: Endpoint override variables can redirect traffic to a different gateway.

Mitigation: Do not run with an untrusted LINKFOX_TOOL_GATEWAY or related endpoint override.

Risk: Search calls consume credits, and larger result limits increase cost.

Mitigation: Start with small limits, confirm the query with the user before expanding pages or result counts, and avoid automatic retries or query rewrites after empty or failed results.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-retrieval-patent-search)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, tabular patent summaries, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can write full API responses under a local linkfox session directory, print compact summaries for larger responses, and cache identical query parameters for 24 hours.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
