## Description:

Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and external users use this skill to count livestock or poultry from barn or passage images and videos, including inventory checks, batch entry or exit counts, and passage counting. It returns structured counting results with totals, confidence, report links, and optional historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm images or videos are processed by a remote cloud API.

Mitigation: Use non-sensitive footage when possible and confirm retention, account handling, and service terms before production use.

Risk: The skill may create or reuse account identity, query account-linked report history, and persist auth or session tokens locally.

Mitigation: Review the skill before installation, restrict workspace access, and prefer explicit user confirmation before historical report lookup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Livestock Counting API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown reports and tables, with JSON available for detailed analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include livestock counts, per-area counts, confidence values, analysis timestamps, and report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
