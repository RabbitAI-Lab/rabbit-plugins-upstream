## Description:

Converts CSV input with headers into a JSON array of objects using Expanso Edge CLI or MCP pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aronchick](https://clawhub.ai/user/aronchick)

### License/Terms of Use:


## Use Case:

Developers and data engineers use this skill to convert CSV data from stdin or HTTP requests into JSON for import/export, API transformation, spreadsheet processing, and log parsing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server mode may expose the converter more broadly than expected because it binds to all network interfaces without authentication or a visible request-size limit.

Mitigation: Prefer CLI mode; if server mode is needed, bind it to 127.0.0.1 or place it behind firewall/authentication controls, and add request-size and rate limits before shared or public exposure.

Risk: The optional cloud deploy command uses a live external pipeline URL.

Mitigation: Review the external pipeline URL and deployment target before using the cloud deploy command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aronchick/skills/expanso-csv-to-json)
- [Expanso Cloud pipeline](https://skills.expanso.io/csv-to-json/pipeline-cli.yaml)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON object containing data, row_count, columns, and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts CSV text with a header row and an optional delimiter; converted values are emitted as strings.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
