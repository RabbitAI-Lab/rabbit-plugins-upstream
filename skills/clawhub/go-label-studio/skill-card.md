## Description:

An unofficial typed Go client for calling the Label Studio API from Go applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate applications with self-hosted or cloud Label Studio installations, including retrieving or managing projects, tasks, annotations, predictions, and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation content are sent to the caller-supplied Label Studio server.

Mitigation: Use a trusted server URL, use HTTPS for remote servers, and keep the API token in protected configuration such as LABEL_STUDIO_API_KEY.

Risk: Creating, updating, or deleting Label Studio resources changes server data.

Mitigation: Make data-changing requests only when requested and only for resources within the user's scope.

Risk: The external Go dependency was not bundled or audited with this release evidence.

Mitigation: Review and pin the dependency version before production use.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project repository](https://github.com/psyb0t/go-label-studio)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, API calls, Configuration instructions, Shell commands]

**Output Format:** [Go code and Markdown guidance with inline shell and Go examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code examples use the Label Studio server URL and API token supplied by the user.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
