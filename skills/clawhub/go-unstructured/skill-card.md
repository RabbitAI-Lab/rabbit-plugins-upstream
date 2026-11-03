## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, generated with oapi-codegen. Package unstructured covers sources, destinations, workflows, jobs, templates, notifications and usage; subpackage partition handles multipart document extraction. Use when Go code needs Unstructured API calls or already imports github.com/psyb0t/go-unstructured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go integrations with Unstructured Platform APIs or partition documents through the Partition API. It provides package setup, authentication, request handling, and endpoint usage guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or selected document contents are sent with requests to Unstructured.

Mitigation: Read the API key from UNSTRUCTURED_API_KEY, keep it out of source code and logs, and upload only documents authorized for processing.

Risk: Connector, workflow, notification, and job operations can change account resources or run work.

Mitigation: Perform these operations only when requested and only on the resources in scope.

Risk: The unofficial Go dependency and referenced upstream materials were not bundled or audited.

Mitigation: Review and pin the dependency version before use.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-unstructured)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with Go code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
