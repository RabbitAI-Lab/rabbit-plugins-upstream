## Description:

Connect Go applications to Label Studio through a typed API client for projects, tasks, annotations, and related operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Go client to connect applications to a trusted Label Studio server and read or manage projects, tasks, annotations, and other API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation data are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL, HTTPS for remote servers, and a token limited to the required resources; keep credentials out of source code and logs.

Risk: Some client operations create, update, or delete server data.

Mitigation: Perform data-changing operations only when requested and within the user's authorized scope.

Risk: The fetched Go dependency was not included in this review.

Mitigation: Pin the dependency version and review updates before adopting them.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go Label Studio project](https://github.com/psyb0t/go-label-studio)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go client calls and setup guidance; endpoint availability varies by Label Studio edition.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
