## Description:

Guides developers in using a Go client for the Supabase Management API to read and manage organizations, projects, branches, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use a typed Go client for Supabase Management API tasks, such as listing projects or managing branches and project configuration. It does not cover per-project data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access tokens or returned secrets could be exposed in source control, logs, or output.

Mitigation: Use scoped OAuth tokens when possible; keep SUPABASE_ACCESS_TOKEN and returned secrets out of source control, logs, and shared output.

Risk: Generated code could change or delete live Supabase project resources.

Mitigation: Review write and destructive calls against the intended project or branch, and run them only when explicitly requested.

## Reference(s):

- [Go Supabase Management on ClawHub](https://clawhub.ai/psyb0t/skills/go-supabase-management)
- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use Supabase Management API operations, not per-project data APIs.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
