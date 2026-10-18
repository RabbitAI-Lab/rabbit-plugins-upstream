## Description:

Helps developers use unofficial Go clients for Unstructured's Platform and Partition APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to write and troubleshoot Unstructured Platform integrations and document-partitioning requests with an unofficial client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating or changing resources and running or cancelling jobs can affect the user's account.

Mitigation: Perform these operations only on user-requested resources, using explicit resource IDs.

Risk: Document uploads send selected file contents to Unstructured.

Mitigation: Upload only files explicitly selected by the user.

Risk: An exposed API key can grant unintended access.

Mitigation: Read the key from the environment; do not hardcode, commit, or log it.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-unstructured)
- [go-unstructured project](https://github.com/psyb0t/go-unstructured)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for client setup, API calls, response handling, and document uploads.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
