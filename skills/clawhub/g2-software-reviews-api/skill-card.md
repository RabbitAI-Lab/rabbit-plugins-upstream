## Description:

Search G2, the B2B software review site, read full product profiles with pricing and features, and pull faceted reviews with exact per-star counts through Scavio's three G2 endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, product researchers, and competitive intelligence teams use this skill to search G2 products, inspect profiles, and retrieve faceted review data for SaaS research and vendor comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key, and exposing unrelated secrets during setup or SDK installation would increase credential risk.

Mitigation: Use an isolated project environment, load SCAVIO_API_KEY from the environment or a secret store, and avoid committing keys in source files.

Risk: G2 requests are described as expensive, and multi-page review pulls can spend credits quickly.

Mitigation: State the expected credit cost before calls, plan the minimum request set, and avoid looping over products or pages without user confirmation.

Risk: Filtered review calls can produce misleading zero-result findings, and product profile calls do not include review text.

Mitigation: Use only documented enum filters, re-check filtered zero-result findings unfiltered, and call the reviews endpoint before drawing conclusions about customer sentiment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/g2-software-reviews-api)
- [Scavio G2 Search Documentation](https://scavio.dev/docs/g2-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=g2-software-reviews-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=g2-software-reviews-api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON endpoint descriptions, shell snippets, and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Scavio G2 API calls that return structured JSON and require the agent to state credit costs before use.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
