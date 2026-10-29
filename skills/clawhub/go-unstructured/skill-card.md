## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, generated with oapi-codegen. Package unstructured covers sources, destinations, workflows, jobs, templates, notifications and usage; subpackage partition handles multipart document extraction. Use when Go code needs Unstructured API calls or already imports github.com/psyb0t/go-unstructured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that calls the Unstructured Platform APIs or partitions documents through the Unstructured Partition API, including guidance on authentication, uploads, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed, selected documents could contain sensitive data, or account resources could be changed.

Mitigation: Keep the API key in UNSTRUCTURED_API_KEY and never log or commit it; upload only files the user authorized for sharing, and limit account changes to requested resources and actions.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [go-unstructured on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [Project homepage](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Guidance, Go code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
