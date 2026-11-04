## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, generated with oapi-codegen. Package unstructured covers sources, destinations, workflows, jobs, templates, notifications and usage; subpackage partition handles multipart document extraction. Use when Go code needs Unstructured API calls or already imports github.com/psyb0t/go-unstructured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with Unstructured Platform resources and the Partition API, including connector and workflow operations and document extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents are sent to Unstructured when upload or partition operations run.

Mitigation: Upload only documents the user authorized for transfer.

Risk: Connector, workflow, notification, and job operations can change account resources or run work.

Mitigation: Limit changes and actions to resources the user specified.

Risk: An exposed API key can grant access to the associated account.

Mitigation: Read the key from UNSTRUCTURED_API_KEY and keep it out of source code, commits, and logs.

Risk: The Go dependency implementation and referenced repository files were not bundled or audited in this release evidence.

Mitigation: Review and pin the dependency before using it.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [Source repository](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the user's Go project and requested Unstructured API operations.]

## Skill Version(s):

0.3.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
