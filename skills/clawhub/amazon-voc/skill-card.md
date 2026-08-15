## Description:

Collects and analyzes Amazon reviews through the ARI service to produce Voice-of-Customer reports, pain points, purchase drivers, personas, trends, competitor comparisons, and listing optimization ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to collect Amazon review data and turn it into actionable consumer insights, competitive findings, and listing or product improvement recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party ARI service and an ARI API key stored in an environment variable or local user configuration.

Mitigation: Install only if the ARI service is trusted, keep the API key private, and avoid including keys in reports, screenshots, or command examples.

Risk: Collection and AI analysis commands can spend ARI credits when confirmed.

Mitigation: Review the quoted price and available balance before running any command with --confirm.

Risk: Review-derived recommendations can be misleading when samples are small, stale, or unavailable for one side of a comparison.

Mitigation: Label small samples clearly, separate direct data from inference and recommendations, and avoid making unsupported claims when the API returns insufficient data.

## Reference(s):

- [Source Repository](https://github.com/funewa/Amazon-VOC)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports, structured JSON responses, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ARI quote details, sample counts, credits used, current balance, ASIN/site context, and archived report identifiers.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
