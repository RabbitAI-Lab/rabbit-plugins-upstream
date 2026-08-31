## Description:

Operate Supabase through an OOMOL-connected account for reading, creating, updating, and deleting Supabase resources by using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer Supabase organizations, projects, Edge Functions, storage buckets, API keys, secrets, health checks, read-only SQL queries, and generated TypeScript database types through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with administrative visibility into connected Supabase projects through OOMOL.

Mitigation: Install it only for accounts and projects where OOMOL-mediated access is acceptable, and avoid connecting projects that the agent should not administer.

Risk: API key, secret, and deletion actions can change or remove Supabase resources.

Mitigation: Review the exact payload and effect before approving write actions, and require explicit approval before destructive actions.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live connector schema before constructing each payload so requests match the current connector contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-supabase)
- [Supabase homepage](https://supabase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON payloads, connector responses, and generated TypeScript types when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before sending action payloads; responses may include connector execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
