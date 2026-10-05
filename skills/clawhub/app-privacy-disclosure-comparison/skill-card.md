## Description:

Compares public App Store privacy labels, Google Play data-safety declarations, and listed Android permissions for selected apps using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app evaluators compare public privacy disclosures across an app shortlist, preserving app identity, original store categories, missing data, and source dates. The comparison is not a verification of actual app behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the third-party lookup service requires an API key and sends search terms to Crawlora.

Mitigation: Use a least-privilege key and avoid unrelated user or device data in queries.

Risk: Public store disclosures and listed permissions may not reflect actual app behavior or establish compliance.

Mitigation: Attribute claims to their source and date, preserve unknowns and differing taxonomies, and verify runtime behavior separately before drawing conclusions.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/app-privacy-disclosure-comparison)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown comparison matrix with explanatory notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source links and dates, platform-specific categories, unknown values, and limits of disclosure-based comparisons.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
