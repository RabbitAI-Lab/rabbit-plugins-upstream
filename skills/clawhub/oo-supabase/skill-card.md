## Description:

Enables agents to operate Supabase projects through OOMOL's oo CLI connector for account, project, database, storage, Edge Function, API key, and secret workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Supabase organizations, projects, database access, storage objects, Edge Functions, API keys, and secrets through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes installer pipe commands for the oo CLI.

Mitigation: Install the oo CLI manually from a trusted source and verify it before allowing an agent to use the connector.

Risk: The skill can operate on sensitive Supabase resources, including API keys, secrets, storage objects, and project data.

Mitigation: Grant connector access only for trusted OOMOL accounts and review requested scopes and targets before use.

Risk: Write and destructive actions can modify or remove Supabase state.

Mitigation: Require explicit user confirmation for each write or destructive action, including the exact payload and expected effect.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-supabase)
- [Supabase Homepage](https://supabase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
