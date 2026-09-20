## Description:

Compare companies or products using Crawlora website extraction, traffic estimates, reviews, product listings, and hiring data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market teams use this skill to produce competitor briefs, positioning and pricing comparisons, and evidence-backed battlecards from official pages and selected third-party data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor URLs, search terms, extraction schemas, and researched page content may be sent to Crawlora along with account-authenticated requests.

Mitigation: Use a dedicated, revocable Crawlora API key and avoid submitting sensitive private pages or confidential business data unless that disclosure is intended.

Risk: Traffic estimates, job postings, reviews, and product discovery results can be stale, sampled, estimated, or incomplete.

Mitigation: Record source URLs, source dates, retrieval time, and evidence type; verify disputed or high-impact claims against primary sources and retain unknowns rather than filling gaps by assumption.

Risk: Using the helper requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment, use a revocable key, and avoid exposing the credential in prompts, logs, or outputs.

## Reference(s):

- [competitor-intelligence endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/competitor-intelligence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown briefs or comparison matrices with source links, claim ledgers, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Material claims should preserve source URLs, source dates, retrieval time, evidence type, and relevant unknowns.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
