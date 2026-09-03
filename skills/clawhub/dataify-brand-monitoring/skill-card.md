## Description:

Monitor a brand across current news, search, reviews, forums, or public social sources and report material mentions, sentiment signals, and reputation risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and business users use this skill to collect bounded public brand-monitoring snapshots, compare recurring runs, and identify material mentions, sentiment signals, coverage gaps, and reputation risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Dataify API token and can spend Dataify credits during public-search runs.

Mitigation: Use dry-run mode, max-action limits, and scoped public source URLs to control cost and exposure.

Risk: Automated mention counts, sentiment signals, and reputation-risk summaries can be incomplete or misleading.

Mitigation: Review generated reports and supporting evidence before making reputation, commercial, pricing, or business decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with generated JSON and Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dated monitoring reports with normalized records, evidence identifiers, metrics, failures, and limitations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
