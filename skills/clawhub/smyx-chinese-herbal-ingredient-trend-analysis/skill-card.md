## Description:

Assesses medicinal-herb leaf images or videos to report estimated active-ingredient accumulation trends and suggest harvest timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, herb cooperatives, and pharmaceutical raw-material teams use leaf images or videos to estimate medicinal-herb accumulation trends, review historical reports, and inform harvest planning. The estimates are visual predictions, not chemical measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Leaf media or supplied URLs are sent to external lifeemergence.com services.

Mitigation: Get permission before submitting sensitive images or URLs and review the service's data-handling terms.

Risk: The skill silently creates or reuses a cloud identity, queries cloud report history, and stores service tokens locally.

Mitigation: Disclose cloud identity and history use, limit access to the local token store, and review token handling before shared deployment.

Risk: Pet-health remnants and inconsistent input handling may cause incorrect or misleading results.

Mitigation: Review the documentation and supported inputs, test on representative herb media, and verify consequential findings independently.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or historical-report list; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated trend level (Low, Medium, High, or Peak) and harvest-timing guidance; reports may include links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
