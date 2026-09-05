## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to query Scavio's G2 endpoints for B2B software discovery, product profiles, pricing, features, alternatives, and review analysis. It is suited for competitive intelligence, voice-of-customer research, product research, and vendor comparison tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party API provider for G2 research.

Mitigation: Install only when third-party API use is acceptable for the intended workflow and data handling requirements.

Risk: API access requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and do not place it in source code.

Risk: Each G2 endpoint call is documented as costing 5 credits, and multi-page review pulls can consume credits quickly.

Mitigation: Plan calls before execution, state the expected credit cost, and avoid broad loops over product or review pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/g2-software-reviews-api)
- [Scavio G2 Search documentation](https://scavio.dev/docs/g2-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=g2-software-reviews-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=g2-software-reviews-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Text, Markdown]

**Output Format:** [Markdown with inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls that return structured JSON from Scavio's G2 endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
