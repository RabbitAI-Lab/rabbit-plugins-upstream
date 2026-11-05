## Description:

Provides unofficial typed Go clients for the Unstructured Platform and Partition APIs for Go applications that manage Platform resources or extract document elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go applications that call Unstructured Platform APIs or partition documents through the Unstructured APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Partition and multipart requests send selected document contents to Unstructured.

Mitigation: Upload only documents the user intends to share with Unstructured.

Risk: The API key enables authenticated API access, and connector, workflow, notification, and job operations can change account resources or run work.

Mitigation: Read the key from UNSTRUCTURED_API_KEY without hardcoding or logging it, and limit account changes to the user-requested resources and actions.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [Module homepage](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API usage, authentication, document upload, and response handling guidance.]

## Skill Version(s):

0.3.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
