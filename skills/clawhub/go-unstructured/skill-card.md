## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, generated with oapi-codegen. Package unstructured covers sources, destinations, workflows, jobs, templates, notifications and usage; subpackage partition handles multipart document extraction. Use when Go code needs Unstructured API calls or already imports github.com/psyb0t/go-unstructured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Go applications with Unstructured Platform APIs and partition documents through its unofficial typed clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client is unofficial and may not match current API behavior.

Mitigation: Review and pin the dependency version before relying on it.

Risk: API credentials and selected document contents are sent to Unstructured services.

Mitigation: Protect UNSTRUCTURED_API_KEY and upload only documents the user intends to share.

Risk: Connector, workflow, notification, job, and upload operations can change account state or transmit data.

Mitigation: Limit these actions to the resources and files explicitly requested by the user.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [Project page](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Go code, API integration guidance, Configuration guidance, Shell commands]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include installation commands, API authentication guidance, and document-upload examples.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
