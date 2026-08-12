## Description:

Analyzes manually provided company candidates, search evidence, domains, LinkedIn links, spreadsheets, CSVs, and existing customer-pool records to deduplicate and prioritize high-fit target companies without automatically writing to the sales pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and CRM operators use this skill to screen manually collected target-company candidates against product fit, market fit, duplicate status, evidence quality, and follow-up priority. It supports human decision-making by surfacing evidence, risks, exclusion reasons, and next steps without making automatic CRM or outreach changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate-company lists and existing customer-pool context may contain commercially sensitive information.

Mitigation: Use the skill only with company and customer-pool context approved for agent processing, and review outputs manually before CRM or outreach changes.

Risk: Company identity, fit, or procurement readiness can be misclassified when evidence is incomplete or based only on search summaries.

Mitigation: Keep unsupported dimensions marked as pending, preserve suspected duplicates, and verify key conclusions against official websites, public research, or internal records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-company-screening)
- [Skill README](artifact/README.md)
- [Examples](artifact/examples.md)
- [Tests](artifact/tests.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown table with evidence-backed screening notes, risk flags, priority recommendations, exclusion reasons, and next steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not automatically write to the sales pipeline, run bulk lookups, or invent missing evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
