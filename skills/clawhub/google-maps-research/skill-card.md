## Description:

Search Google Maps places through Crawlora to compare current business details, ratings, review samples, and photos with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and business users compare places by address, ratings, and available business details, using sampled reviews or photos when relevant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Place queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when sharing those queries and the key with Crawlora is acceptable; keep the key in the environment.

Risk: Search results, reviews, and photos are current samples rather than complete archives.

Mitigation: Include retrieval time and source links; avoid treating samples as exhaustive or representative.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/google-maps-research)
- [Crawlora](https://crawlora.net)
- [Google Maps endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown comparison or concise text with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include retrieval time and distinguish missing details from confirmed facts.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
