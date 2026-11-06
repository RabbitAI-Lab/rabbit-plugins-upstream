## Description:

Unofficial Go clients for the Unstructured Platform and Partition APIs, covering platform operations and multipart document extraction for Go projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to write Go code that integrates with the Unstructured Platform APIs or partitions documents through the Unstructured Partition API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Partition requests send the selected document contents to Unstructured.

Mitigation: Upload only documents the user intends to share with Unstructured.

Risk: The API key grants access to the Unstructured account.

Mitigation: Read it from UNSTRUCTURED_API_KEY and never hardcode, commit, or log it.

Risk: Connector, workflow, notification, and job operations can change account state or initiate processing.

Mitigation: Perform those operations only when requested, and only for resources within the user's scope.

Risk: The external Go dependency and repository examples were not audited.

Mitigation: Review them before relying on their behavior.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [Project page](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples, shell commands, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
