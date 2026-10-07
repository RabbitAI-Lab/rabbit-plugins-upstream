## Description:

Compares app review themes around documented releases using Crawlora version notes and live or stored reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams, analysts, and developers use this skill to compare sampled App Store and Google Play feedback around app releases while preserving version attribution and causal limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API receives the API key and requested app IDs, search terms, locations, languages, and review queries.

Mitigation: Use a key intended for Crawlora and limit requests to intended public app-review research; avoid sensitive query text.

Risk: Broad review requests can consume credits and produce unrepresentative comparisons.

Mitigation: Set page and credit limits, apply comparable sampling rules, and disclose selection bias and missing release history.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/app-release-feedback-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated release ledger, comparable review-theme counts, cited excerpts, sampling disclosures, and causal caveats.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
