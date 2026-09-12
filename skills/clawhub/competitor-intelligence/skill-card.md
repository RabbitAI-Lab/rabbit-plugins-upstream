## Description:

Compare companies or products using Crawlora website extraction, traffic estimates, reviews, product listings, and hiring data. Use for competitor briefs, positioning and pricing comparisons, or evidence-backed competitive battlecards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and analysts use this skill to prepare competitor briefs, comparison matrices, positioning reviews, pricing checks, and evidence-backed battlecards from selected public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor names, search terms, public page URLs, and extraction requests are sent to Crawlora with the user's API key.

Mitigation: Avoid confidential strategy, secrets, customer data, and non-public documents; keep requests limited to public sources needed for the brief.

Risk: Traffic estimates, review samples, Product Hunt alternatives, and job listings can be stale, incomplete, or unsuitable as direct measurements of business performance.

Mitigation: Label these signals by source and retrieval time, verify high-impact claims against primary pages, and preserve unknowns or disagreements instead of forcing a single score.

Risk: Broad competitor research can collect more third-party data than the user's decision requires.

Mitigation: Use explicit locale and narrow source choices, and bound pages and enrichments to the requested brief.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/competitor-intelligence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with comparison tables, sourced claim ledgers, concise prose, and inline shell commands where API calls are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON returned from Crawlora helper calls as supporting evidence for the agent's analysis.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
