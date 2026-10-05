## Description:

Analyzes farm camera images and videos to count livestock or poultry and report inventory totals with confidence estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and their agents use barn or passage camera footage to estimate livestock headcounts, review confidence and area-level counts, and retrieve historical inventory reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm media and report queries are sent to external lifeemergence.com services.

Mitigation: Review the service's data-handling terms and obtain approval before processing sensitive farm media or historical reports.

Risk: The skill silently creates or reuses an identity and persists authentication tokens in a workspace database.

Mitigation: Run only in an approved workspace with appropriate access controls and credential-retention practices.

Risk: Dense groups, occlusion, or poor camera conditions can make counts unreliable.

Mitigation: Use stable, well-lit footage and verify results against existing counting procedures before updating official records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured counting report or Markdown table of historical reports; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include total and area counts, confidence estimates, and report links; counts require human review for official inventory records.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
