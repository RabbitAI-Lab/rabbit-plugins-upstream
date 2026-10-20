## Description:

An unofficial Go client skill for using the Supabase Management API to inspect and manage Supabase organizations, projects, branches, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Help Go developers write code that uses the Supabase Management API to inspect or manage organizations, projects, branches, and project settings. The skill does not target Supabase's per-project data APIs. Use live-changing operations only when the user explicitly authorizes the change and target project.

### Deployment Geography for Use:

The skill specifies no geographic restriction; availability and applicable requirements depend on Supabase services and the user's operating environment.

## Known Risks and Mitigations:

Risk: Supabase access tokens can grant sensitive Management API access.

Mitigation: Keep tokens secret, use the narrowest suitable OAuth scopes or permissions, and provide credentials through a secure mechanism.

Risk: Write operations can change or remove live project resources or data.

Mitigation: Confirm the exact target project and requested change; perform mutating operations only with explicit user authorization.

Risk: The Go client is an external dependency.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Supabase Management API authentication guidance](https://supabase.com/docs/reference/api/introduction)
- [go-supabase-management package](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-supabase-management)

## Skill Output:

**Output Type(s):** [code, text, configuration, guidance]

**Output Format:** [Go source snippets and concise setup or usage instructions, typically in Markdown.]

**Output Parameters:** [Go API operation, relevant organization or project reference, and the user-authorized change when a write operation is requested.]

**Other Properties Related to Output:** [Uses a Supabase access token; token scope and permissions determine accessible operations.]

## Skill Version(s):

0.3.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
