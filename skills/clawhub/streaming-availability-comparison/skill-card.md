## Description:

Compares movie, show, season, and episode viewing offers across countries and providers using Crawlora JustWatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Viewers and researchers use this skill to compare where specific titles or episodes can be watched in selected countries, including provider, purchase or subscription basis, and missing offer details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup requests send title queries and a Crawlora API key to Crawlora.

Mitigation: Use the skill only if comfortable sharing those data with Crawlora; omit sensitive personal details from query parameters and limit shell approval to the bundled helper and requested lookup scope.

Risk: Regional offer data may omit conditions or change after observation.

Mitigation: Preserve source and observation times, distinguish offer types and unknown conditions, and confirm availability and price with the provider before acting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/streaming-availability-comparison)
- [Crawlora JustWatch endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison matrix and shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes offer type, provider, country, title or episode scope, source and observation time, and missing conditions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
