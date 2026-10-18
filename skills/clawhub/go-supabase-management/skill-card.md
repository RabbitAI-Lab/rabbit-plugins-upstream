## Description:

Guides Go developers in using a typed client to manage Supabase organizations, projects, branches, and settings through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add a Go client for listing and managing Supabase organizations, projects, branches, and project configuration. It does not cover the per-project data API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access tokens and returned secrets could be exposed in source code or logs.

Mitigation: Load tokens from the environment, prefer narrowly scoped OAuth access where available, and keep tokens, request headers, and secret values out of commits and logs.

Risk: Management operations can change or delete live projects and incur billing changes.

Mitigation: Require explicit user confirmation for destructive, configuration, billing, secret, or query-writing actions, and verify the intended project or branch before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-supabase-management)
- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Supabase Management API, not the per-project data API.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
