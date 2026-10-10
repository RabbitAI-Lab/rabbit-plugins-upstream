## Description:

Maps artist discographies and comparable music releases using Crawlora's Spotify catalog lookups for sourced release-cohort and catalog-positioning briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Music researchers and release analysts compare public artist catalogs, release types, editions, and available positioning signals while preserving identity, date precision, and source limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Catalog queries go to an external service and require a Crawlora API key.

Mitigation: Protect the key as a credential and avoid sensitive private search terms.

Risk: Incomplete catalog coverage or mismatched release editions and public metrics could mislead comparisons.

Mitigation: Verify artist and recording identities, retain source and observation dates, and label coverage gaps and metric limitations.

## Reference(s):

- [Spotify endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/music-release-landscape)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown brief with catalog matrix, identity and coverage ledgers, sourced hypotheses, and unknowns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves release-date precision and distinguishes primary releases, appearances, recordings, and editions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
