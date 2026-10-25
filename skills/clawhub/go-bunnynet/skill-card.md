## Description:

Writes Go code with go-bunnynet (package bunnynet, github.com/psyb0t/go-bunnynet), an unofficial generated client for the Bunny.net core API covering CDN pull zones, cache purges, DNS, storage and video library configuration, statistics, load balancers and billing. Use when a Go project imports go-bunnynet or needs Bunny.net core API calls. Excludes storage file transfers and the separate Stream API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that integrates with Bunny.net's core API through the go-bunnynet client, including resource management, statistics, and billing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The account key can authorize consequential changes to Bunny.net resources.

Mitigation: Keep requests specific, perform account-changing operations only when requested, and review generated mutation code before running it. Keep credentials out of source and logs.

Risk: The Go client is unofficial, and the security verdict covers the bundled skill instructions rather than the dependency itself.

Mitigation: Review and pin the Go dependency separately.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)
- [Skill homepage](https://github.com/psyb0t/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Go API usage examples and account-operation guidance; does not itself execute or produce project files.]

## Skill Version(s):

0.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
