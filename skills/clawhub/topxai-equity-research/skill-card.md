## Description:

Guides agents through sourced equity, industry, and macro research, including valuation, adversarial review, and tracking research calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unbelievablet](https://clawhub.ai/user/unbelievablet)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to produce evidence-backed company, industry, and macro reports, challenge investment theses, and maintain a record of research calls. Its ratings are research judgments, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research records and cached market data persist in the project.

Mitigation: Review generated files and periodically clear or review research/desk/cache/sec when local persistence matters.

Risk: The workflow can contact external market-data services and needs credentials for some data sources.

Mitigation: Approve external data access and supply SEC/FRED credentials only through environment variables.

Risk: Broad instructions may prompt edits to installed skill files or automated ledger and scheduler changes.

Mitigation: Review changes before permitting skill-file edits, ledger settlement, or scheduler setup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/unbelievablet/skills/topxai-equity-research)
- [Publisher homepage](https://ai.topxea.com)
- [Research framework](references/framework.md)
- [Research quality bar](references/quality-bar.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown research reports and checklists, JSON research records, and operational commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports report updates, coverage monitoring, and settlement of research calls.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
