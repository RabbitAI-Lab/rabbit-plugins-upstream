## Description:

Compares job offers by calculating cost-of-living adjusted compensation, effective hourly rate, PTO value, and break-even base salary targets for negotiation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and agents use this skill to compare job offers with different salary, benefits, commute, relocation, and cost-of-living assumptions. It supports negotiation by producing a break-even salary number and decision-oriented compensation metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Offer inputs may contain sensitive compensation, benefits, commute, or relocation details.

Mitigation: Use only the offer JSON needed for comparison and avoid placing unrelated sensitive documents or personal data in the input file.

Risk: Incorrect assumptions about bonus attainment, equity risk, cost of living, commute, or overtime can produce misleading negotiation guidance.

Mitigation: Verify inputs against offer documents and treat outputs as decision support, not tax, investment, or financial advice.

Risk: The workflow may execute the bundled local Python comparator.

Mitigation: Review commands before execution and run the skill in a trusted local workspace.

## Reference(s):

- [Compensation Model](references/compensation-model.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/job-offer-comparator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, plain text comparison tables, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Python comparator; no third-party dependencies or network access documented.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
