## Description:

Prepare customer record fields and assemble reporting export rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to prepare customer record fields from user-provided notes and assemble concise reporting export rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer data could be included beyond the information intentionally supplied for the current request.

Mitigation: Use only customer data the user intentionally provides in the current request.

Risk: A preparation or export stage could be invoked when the user did not clearly request that stage.

Mitigation: Invoke only the specific stage the user clearly asks for.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/customer-report-export-desk)

## Skill Output:

**Output Type(s):** [text, JSON-compatible structured data]

**Output Format:** [Structured fields for record_field and export_row]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces concise customer reporting objects including record_id, field_name, field_value, columns, row_values, and row_digest.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
