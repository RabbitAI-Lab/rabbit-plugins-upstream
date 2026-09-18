## Description:

Supabase (supabase.com). Use this skill for ANY Supabase request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Supabase projects through an OOMOL-connected account, including projects, organizations, API keys, secrets, Edge Functions, regions, health checks, database queries, generated TypeScript types, and storage resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands.

Mitigation: Review the installer before use or prefer a verified package-managed oo CLI installation.

Risk: The skill can perform sensitive Supabase administration actions, including API key, secret, storage, and project changes.

Mitigation: Confirm the exact project, key, secret, storage object, payload, and expected effect before approving write or destructive actions.

## Reference(s):

- [ClawHub Supabase Skill](https://clawhub.ai/oomol/skills/oo-supabase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Supabase](https://supabase.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands that inspect live action schemas and run Supabase connector actions; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.6 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
