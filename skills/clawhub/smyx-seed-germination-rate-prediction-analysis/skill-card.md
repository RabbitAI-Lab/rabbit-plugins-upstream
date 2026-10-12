## Description:

Analyzes seedling-tray images or videos to count emerged seedlings and estimate germination rates from the number of seeds sown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, seed-testing teams, and greenhouse operators use seedling-tray media to estimate emergence and germination rates and review previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Seedling media or media URLs are sent to cloud services for analysis.

Mitigation: Obtain approval before sharing media and use only media and URLs cleared for cloud processing.

Risk: The skill silently creates or reuses a local identity and stores account tokens in a workspace SQLite database.

Mitigation: Install only where this identity and token handling is acceptable, and limit access to the workspace and stored tokens.

Risk: Historical report queries can retrieve cloud-stored report history.

Mitigation: Limit report queries and access to users authorized to view that history.

## Reference(s):

- [Skill listing](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report or Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include seedling counts, estimated germination rates, and report links; results are for reference, not planting advice.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
