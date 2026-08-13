## Description:

Deep consumer insights from pre-analyzed Amazon reviews, extracting pain points, buying factors, user profiles, usage patterns, differentiation opportunities, competitor sentiment, and listing-copy suggestions through ZooData.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and product teams use this skill to analyze Amazon reviews for single ASINs, competitor sets, or product categories. It produces customer-feedback intelligence, product-improvement signals, positioning guidance, and listing-copy suggestions from ZooData API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a ZooData API key and sends product identifiers, category paths, marketplace/date filters, and numeric filters to ZooData.

Mitigation: Install only where ZooData API use is acceptable, use a dedicated key, and keep credentials in the supported environment or local config path.

Risk: Review analysis can consume ZooData credits, especially multi-call deep dives and optional endpoint probes.

Mitigation: Confirm estimated credit use before broad scans, avoid optional endpoint probes unless diagnosing setup, and prefer granular commands when tighter credit control is needed.

Risk: Business recommendations may be incomplete or misleading when API coverage is sparse or fallback samples are small.

Mitigation: Report only returned evidence, surface sample-size and data-provenance notes, and validate important business decisions with additional sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor)
- [Project homepage from metadata](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API field reference](references/reference.md)
- [ZooData CLI contract](references/cli-contract.md)
- [ZooData](https://zoodata.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with structured tables, API provenance, confidence labels, and optional JSON intermediates from the bundled CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; ZooData API calls consume account credits.]

## Skill Version(s):

1.0.9 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
