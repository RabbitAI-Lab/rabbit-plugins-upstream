## Description:

Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API for current place lookups and comparisons, including addresses, ratings, review themes, and business information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research current Google Maps places through Crawlora, compare candidate businesses, and report addresses, ratings, review samples, photos, source URLs, and unknown fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Maps search terms, place IDs, review queries, photo requests, and related request bodies are sent to Crawlora using the user's Crawlora API key.

Mitigation: Install only when that data sharing is acceptable, keep the key scoped to Crawlora, and avoid sending unrelated private data in request bodies.

Risk: Review and search outputs can be incomplete snapshots, so treating them as exhaustive evidence may mislead downstream decisions.

Mitigation: Report retrieval time, source URLs, unknown fields, and the documented limits of search results and review samples.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/google-maps-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables and inline shell command examples; the helper returns JSON from Crawlora.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include retrieval time, source URLs, ratings and review counts together, and unknowns for unavailable fields. Search results are snapshots, and review samples are not complete or representative surveys.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
