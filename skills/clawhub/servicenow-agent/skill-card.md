## Description: <br>
Read-only CLI access to ServiceNow Table, Attachment, Aggregate, and Service Catalog APIs; includes schema inspection and history retrieval (read-only). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to read ServiceNow records, attachment metadata or content, aggregate statistics, service catalog details, schemas, and ticket history from a configured ServiceNow instance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled OpenAPI references include POST, PUT, PATCH, and DELETE operations despite the skill's read-only framing. <br>
Mitigation: Restrict agent use to documented GET workflows and do not expose write or delete operations unless a write-capable integration is intentionally approved. <br>
Risk: ServiceNow credentials could grant broader access than the skill needs. <br>
Mitigation: Use a dedicated read-only ServiceNow account and avoid admin credentials. <br>
Risk: Downloaded attachments and ticket history may contain sensitive operational or personal data. <br>
Mitigation: Treat saved attachment files and history outputs as sensitive data and apply local retention and access controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/servicenow-agent) <br>
- [Publisher profile](https://clawhub.ai/user/thesethrose) <br>
- [ServiceNow Table API documentation](https://docs.servicenow.com/?context=CSHelp:REST-Table-API) <br>
- [ServiceNow Attachment API documentation](https://docs.servicenow.com/?context=CSHelp:REST-Attachment-API) <br>
- [ServiceNow Aggregate API documentation](https://docs.servicenow.com/?context=CSHelp:REST-Aggregate-API) <br>
- [Table API OpenAPI reference](artifact/references/table-api.yaml) <br>
- [Attachment API OpenAPI reference](artifact/references/attachment.yaml) <br>
- [Aggregate API OpenAPI reference](artifact/references/aggregate-api.yaml) <br>
- [Service Catalog API OpenAPI reference](artifact/references/service-catalog-api.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [JSON responses, shell commands, and optional saved binary attachment files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pretty-printed JSON is available with --pretty; attachment content can be written to a caller-provided path with --out.] <br>

## Skill Version(s): <br>
0.1.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
