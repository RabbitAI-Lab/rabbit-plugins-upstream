## Description:

Writes Go code with go-bunnynet (package bunnynet, github.com/psyb0t/go-bunnynet), an unofficial generated client for the Bunny.net core API covering CDN pull zones, cache purges, DNS, storage and video library configuration, statistics, load balancers and billing. Use when a Go project imports go-bunnynet or needs Bunny.net core API calls. Excludes storage file transfers and the separate Stream API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go integrations with Bunny.net's core API through the go-bunnynet client, including pull zone, DNS, storage configuration, statistics, and billing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Bunny.net account API key could allow unauthorized access to account resources.

Mitigation: Read BUNNYNET_API_KEY from the environment and never hardcode or log credentials.

Risk: Creating, changing, or deleting resources and purging caches affect the user's Bunny.net account.

Mitigation: Make account-changing calls only when requested, and check the intended resource and operation before proceeding.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-bunnynet package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)
- [go-bunnynet source repository](https://github.com/psyb0t/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the project's Go code and requested Bunny.net core API operations.]

## Skill Version(s):

0.3.5 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
