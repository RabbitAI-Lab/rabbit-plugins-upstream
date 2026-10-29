## Description:

Guides Go developers in using the unofficial go-render-api client to call Render’s public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or work with Go code that calls Render’s public API, including service and deploy operations. It provides setup, authentication, pagination, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Render API credentials could be exposed or sent to an unintended endpoint.

Mitigation: Keep the API key secret and send authenticated requests only to the intended Render endpoint.

Risk: Deploy, suspend, scale, update, or delete operations can change live infrastructure.

Mitigation: Name the exact services and actions to authorize, and perform them only when requested.

Risk: An unreviewed dependency version may introduce unexpected changes.

Mitigation: Consider pinning a reviewed dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-render-api package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)
- [Project homepage](https://github.com/psyb0t/go-render-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include examples for authenticated Render API requests and operations that affect live services.]

## Skill Version(s):

0.4.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
