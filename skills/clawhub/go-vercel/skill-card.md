## Description:

Guides Go developers in using go-vercel, a typed client for the Vercel REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the skill to add typed Vercel API calls to applications, including project, deployment, domain, and team operations. It provides setup, authentication, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel token could be exposed or used against the wrong personal account or team.

Mitigation: Use a token limited to the needed resources, keep it in an environment variable, and verify the intended account or team.

Risk: Some Vercel API operations change or delete live resources.

Mitigation: Confirm the intended resource and obtain an explicit request before making live changes.

Risk: The external Go dependency implementation is outside the documentation security assessment.

Mitigation: Review and pin the fetched Go dependency.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance, Usage guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover setup, bearer-token authentication, team selection, and response handling.]

## Skill Version(s):

0.19.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
