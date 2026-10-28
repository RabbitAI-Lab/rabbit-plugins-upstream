## Description:

Writes Go code with go-bunnynet (package bunnynet, github.com/psyb0t/go-bunnynet), an unofficial generated client for the Bunny.net core API covering CDN pull zones, cache purges, DNS, storage and video library configuration, statistics, load balancers and billing. Use when a Go project imports go-bunnynet or needs Bunny.net core API calls. Excludes storage file transfers and the separate Stream API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go code that calls Bunny.net core API endpoints through the go-bunnynet client, including CDN, DNS, storage configuration, statistics, and billing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Bunny.net API key can grant account access.

Mitigation: Read BUNNYNET_API_KEY from the environment and never hardcode or log credentials.

Risk: Creating, changing, deleting, or purging resources can affect the user's Bunny.net account.

Mitigation: Perform account changes only when requested, and confirm the intended resources and operation.

Risk: The client is unofficial and generated, so dependency or API behavior may need review.

Mitigation: Review and pin the Go dependency, consult the operation documentation, and check HTTP status and decoded response fields.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-bunnynet package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)
- [go-bunnynet source repository](https://github.com/psyb0t/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-changing API calls; execute them only when requested.]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
