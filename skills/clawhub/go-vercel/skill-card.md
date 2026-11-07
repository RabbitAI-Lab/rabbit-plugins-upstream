## Description:

Guides Go developers in using the unofficial go-vercel client to call Vercel's REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Vercel REST API calls to Go projects, including project, deployment, domain, DNS, environment variable, and team operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked or overly broad Vercel token could expose account or team resources.

Mitigation: Use a narrowly scoped token, keep it out of logs and source control, and confirm the intended account or team before making changes.

Risk: Some API operations can change or delete live resources, and the downloaded Go dependency has not been audited by this assessment.

Mitigation: Limit changes to resources the user asked about, and review and pin the external Go dependency.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel source repository](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown guidance with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers bearer-token setup, optional team selection, typed requests and responses, and API error handling.]

## Skill Version(s):

0.21.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
