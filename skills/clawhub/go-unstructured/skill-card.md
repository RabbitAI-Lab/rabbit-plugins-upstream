## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, generated with oapi-codegen. Package unstructured covers sources, destinations, workflows, jobs, templates, notifications and usage; subpackage partition handles multipart document extraction. Use when Go code needs Unstructured API calls or already imports github.com/psyb0t/go-unstructured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the unofficial typed Unstructured Platform and Partition clients into Go projects. It helps with API operations, document partitioning, uploads, and related request handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This is an unofficial client and its dependency may change.

Mitigation: Review the client and pin the dependency version before using it.

Risk: API credentials could be exposed, or requests could affect unintended account resources.

Mitigation: Keep the API key in an environment variable, never hardcode or log it, and specify only the exact resources and actions the user requested.

Risk: Partition and workflow uploads send document contents to Unstructured services.

Mitigation: Upload only documents the user is authorized to share.

## Reference(s):

- [Setup and reference guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [code, guidance, shell commands, configuration]

**Output Format:** [Go source code and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dependency installation and API request examples; requests can upload selected documents or modify account resources.]

## Skill Version(s):

0.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
