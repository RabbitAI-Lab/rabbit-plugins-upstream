## Description:

Analyzes seed tray images or videos to count emerged seedlings, estimate germination rates, and provide structured reports and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, seed companies, and nursery operators can analyze seed tray imagery to estimate germination rates, review seedling counts, and access historical reports. Results are visual estimates for seed-quality reference, not agricultural planting advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Seed tray images or URLs are sent to the vendor's cloud service for analysis.

Mitigation: Use only media you are comfortable sharing with the vendor; check for sensitive content before submission.

Risk: The skill can silently create or reuse a local identity and retain service tokens for cloud report history.

Mitigation: Review persistent account linkage before use; remove data/smyx-api-key.txt and the workspace SQLite database when that linkage is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis)
- [Seed germination analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown table of historical reports, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emerged-seedling counts, germination-rate estimates, alerts, and links to cloud reports.]

## Skill Version(s):

1.0.15 (source: ClawHub release; bundled frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
