## Description:

Writes Go code with go-bunnynet (package bunnynet, github.com/psyb0t/go-bunnynet), an unofficial generated client for the Bunny.net core API covering CDN pull zones, cache purges, DNS, storage and video library configuration, statistics, load balancers and billing. Use when a Go project imports go-bunnynet or needs Bunny.net core API calls. Excludes storage file transfers and the separate Stream API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go code that calls Bunny.net core APIs through the unofficial go-bunnynet client, including CDN, DNS, storage configuration, video library configuration, statistics, load balancers, and billing. It also guides installation, authentication, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Bunny.net account key can authorize consequential account and resource changes.

Mitigation: Keep BUNNYNET_API_KEY private; do not hardcode or log credentials, and perform mutations, cache purges, key rotation, or account closure only when requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-bunnynet source repository](https://github.com/psyb0t/go-bunnynet)
- [go-bunnynet package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code for Bunny.net core API requests; storage file transfers and the separate Stream API are outside scope.]

## Skill Version(s):

0.3.4 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
