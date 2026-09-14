## Description:

Researches public local-business profiles, ratings, reviews, complaints, scam reports, menus, and photos across Yelp, BBB, Trustpilot, and OpenTable using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare local businesses, restaurants, and service providers for vendor due diligence, reputation checks, and source-bounded review summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, business identifiers, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only organization-approved target lists and investigative terms, avoid confidential or sensitive inputs, and store and rotate the Crawlora API key as a secret.

Risk: Platform ratings, reviews, complaints, and scam reports may be incomplete, moderated, duplicated, or attached to the wrong branch.

Mitigation: Keep each platform separate, preserve collection time and source URL or ID, flag unresolved identity matches, and avoid conclusions based on a single review or rating.

Risk: Review text may contain personal information about private individuals.

Mitigation: Quote only what is needed for a business-level finding and avoid identifying private individuals from review text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/local-business-reputation-research)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reputation brief with linked source excerpts and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific ratings, review excerpts, complaint summaries, unresolved identity matches, collection times, and source URLs or IDs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
