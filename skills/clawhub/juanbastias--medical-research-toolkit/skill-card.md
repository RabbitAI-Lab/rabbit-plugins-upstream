## Description:

Search 14+ biomedical databases through a unified MCP endpoint for drug repurposing, target discovery, clinical trials, biomedical literature, genetic associations, and compound activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juanbastias](https://clawhub.ai/user/juanbastias)

### License/Terms of Use:

MIT-0

## Use Case:

Biomedical researchers and developers use the skill to search literature, disease targets, drug activity, clinical trials, and related biomedical records across integrated databases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests are sent to a third-party hosted MCP endpoint and handled by its operator.

Mitigation: Use only non-identifying public research terms; do not send patient records, private files, passwords, or API keys.

Risk: The security review had incomplete coverage, so it could not establish that all referenced material was reviewed.

Mitigation: Review the skill and relevant external material before relying on it, and validate response schemas and source records.

## Reference(s):

- [Hosted unified MCP endpoint](https://mcp.cloud.curiloo.com/tools/unified/mcp)
- [OMIM API](https://omim.org/api)
- [OpenFDA](https://open.fda.gov)
- [NCI Clinical Trials API](https://clinicaltrialsapi.cancer.gov)

## Skill Output:

**Output Type(s):** [Text, Research guidance, Shell commands, Biomedical search results]

**Output Format:** [Markdown guidance with inline curl examples and returned research records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the hosted service and selected databases; validate response schemas and source records before reporting findings.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
