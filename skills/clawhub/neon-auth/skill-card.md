## Description:

Guides developers in adding Neon Auth to apps while preserving existing identity providers unless migration is requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to implement Neon Auth sign-up, sign-in, and protected routes in new apps, or plan an explicitly requested authentication migration. It distinguishes managed from self-managed options and preserves an existing working provider by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to fetch or install a separate parent Neon skill before use.

Mitigation: Review or pin the parent skill's content before allowing the agent to load it.

Risk: Auth migrations or changes to trusted domains, deployments, or environment settings can disrupt login or alter access.

Mitigation: Review these changes before applying them and replace an existing identity provider only when explicitly requested.

## Reference(s):

- [Parent Neon skill](https://neon.com/docs/ai/skills/neon/SKILL.md)
- [Managed Auth implementation guide](references/managed-auth.md)
- [Self-managed Better Auth guide](references/self-managed.md)
- [Neon Auth overview](https://neon.com/docs/auth/overview.md)
- [Neon Auth production checklist](https://neon.com/docs/auth/production-checklist.md)
- [Migration from Supabase Auth](https://neon.com/docs/auth/migrate/from-supabase.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code snippets and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Steps depend on the app's existing identity provider and required auth features.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
