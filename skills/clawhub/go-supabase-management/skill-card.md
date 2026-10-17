## Description:

Guides Go developers in using an unofficial typed client to manage Supabase organizations, projects, branches, and settings through the Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add a Go client for listing and managing Supabase organizations, projects, branches, and project settings. It does not cover a project's data, Auth, or Storage APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A personal access token may grant broad control over Supabase organizations and expose sensitive credentials.

Mitigation: Prefer scoped OAuth tokens when possible; keep tokens and returned secrets out of code, logs, and shared output.

Risk: Write operations can delete, pause, reset, or merge live resources, execute queries, or change secrets.

Mitigation: Perform these operations only after explicit user approval for the specified project or branch.

Risk: Installing an unofficial Go module introduces a third-party dependency.

Mitigation: Verify the module source before adding it to a project.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-supabase-management)
- [Go Supabase Management module](https://github.com/psyb0t/go-supabase-management)
- [Setup and API reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Supabase access token; the skill guides code changes rather than generating files itself.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
