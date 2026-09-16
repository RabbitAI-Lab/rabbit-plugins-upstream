## Description:

Use this skill to operate Supabase for reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Supabase projects, organizations, API keys, secrets, Edge Functions, storage resources, health checks, read-only SQL queries, and TypeScript database type generation through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running unverified remote installer scripts in a shell.

Mitigation: Install the oo CLI through a verified official package, or download and inspect a versioned installer with a checksum or signature before execution.

Risk: Write and destructive Supabase actions can modify or delete project resources, API keys, secrets, or storage objects.

Mitigation: Confirm the exact project, resource, action, and payload with the user before approving write or destructive operations.

## Reference(s):

- [Supabase homepage](https://supabase.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-supabase)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads and to confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.6 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
