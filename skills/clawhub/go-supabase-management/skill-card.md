## Description:

Guides Go agents in using an unofficial typed client for Supabase organization, project, branch, and settings management through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that lists or manages Supabase organizations, projects, branches, and project settings with the typed Management API client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A personal access token can access all organizations available to its user, and write operations can change live projects.

Mitigation: Prefer an OAuth token scoped to the needed permissions, and confirm the exact project or branch and intended change before write operations.

Risk: Tokens and API responses can contain credentials or other secrets.

Mitigation: Read tokens from the environment and keep credentials, request headers, and returned secrets out of logs.

Risk: The unofficial Go dependency's downloaded code was not audited in the supplied security review.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Go client repository](https://github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single stream of task guidance; does not itself execute API operations.]

## Skill Version(s):

0.3.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
