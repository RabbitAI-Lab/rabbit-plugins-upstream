## Description:

Guides Go developers in using an unofficial typed client for Supabase's Management API to inspect and manage organizations, projects, branches, and project settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install the unofficial typed client and write code that lists or manages Supabase organizations, projects, branches, and project settings. It covers the Management API, not per-project data APIs such as PostgREST, Auth, or Storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal access tokens can grant broad access across the user's organizations, and credentials or returned secrets could be exposed if logged or committed.

Mitigation: Prefer an appropriately scoped OAuth token where practical; otherwise use a narrowly scoped credential, read it from the environment, and never log or commit tokens or secret values.

Risk: Write operations can change live Supabase projects, including destructive or security-sensitive settings.

Mitigation: Confirm the requested operation and exact project or branch before making a write; require explicit user direction for live changes.

Risk: The unofficial Go dependency is outside the security assessment of the bundled skill instructions.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference guide](references/setup.md)
- [Go client project homepage](https://github.com/psyb0t/go-supabase-management)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Supabase API authentication](https://supabase.com/docs/reference/api/introduction)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
