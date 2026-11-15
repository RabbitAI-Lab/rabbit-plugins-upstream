## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers and agronomists can analyze top-view field images or videos to identify weeds, estimate coverage and distribution, and review structured results for field management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags remote data transmission and account or token handling; local field media may be sent for analysis.

Mitigation: Before use, confirm what media and identity or account data the service sends or stores, and avoid sensitive imagery until the data handling is understood.

Risk: The security review notes that an export-only option may still run analysis.

Mitigation: Confirm the option's behavior before execution; do not rely on it to prevent analysis or data transmission without verification.

Risk: The security review had partial coverage because a referenced path was missing.

Mitigation: Review the missing path and obtain a complete scan before relying on the review as covering the full release.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Structured analysis results and report listings with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results can include weed categories, coverage and distribution data, and heatmap data; historical report results may include export links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
