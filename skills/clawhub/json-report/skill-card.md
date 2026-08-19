## Description:

Convert JSON data into clean Markdown tables and reports. Use for pasted JSON, API or log output, or any batch of JSON records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dwzhjt](https://clawhub.ai/user/dwzhjt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and documentation authors use this skill to turn pasted JSON, API responses, logs, exports, or batches of JSON records into readable Markdown reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Markdown can expose sensitive values present in the source JSON.

Mitigation: Run the skill only on JSON whose values are intended to appear in the report, and review or redact the output before sharing.

Risk: Mixed record shapes, nested objects, or large inputs can produce sparse or very wide Markdown tables.

Mitigation: Inspect the generated table structure and choose a key/value or split-table layout when that is clearer for readers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dwzhjt/skills/json-report)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown report with an optional title and one or more GitHub-style tables, delivered as markdown text or a .md file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source field names and values, escapes table-breaking characters, and converts multi-line cell values to <br>.]

## Skill Version(s):

1.0.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
