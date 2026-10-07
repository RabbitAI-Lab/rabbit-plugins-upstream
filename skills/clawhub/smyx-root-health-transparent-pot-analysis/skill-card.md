## Description:

Analyzes images or videos of plant roots in transparent pots or seedling boxes to assess visible root condition, assign a health score and vitality grade, and suggest care adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Plant growers and cultivation teams use the skill to review root images or videos for visible signs of decline and receive a health assessment and care guidance. They can also retrieve previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report history are sent to a vendor cloud service.

Mitigation: Review the service endpoints and retention model before use; avoid sensitive media unless cloud processing is acceptable.

Risk: The skill silently creates or reuses an account identity and stores service tokens locally.

Mitigation: Review account and local token storage before installation and limit access to the environment where it runs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured assessment text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Root health score (0–100), vitality grade, care guidance, and report links; optional saved output file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release metadata; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
