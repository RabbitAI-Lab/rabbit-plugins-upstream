## Description:

Helps developers add authentication to applications using Neon, choose an identity provider, and implement supported login flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add authentication to Neon applications, preserve working identity providers when appropriate, and choose Managed Better Auth or a self-managed option when a required feature is unsupported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication changes may target the wrong project or branch, or be deployed without sufficient review.

Mitigation: Confirm the intended project and branch, and review authentication changes before production deployment.

Risk: Secrets may be exposed through browser code, repositories, or logs.

Mitigation: Keep secrets outside browser code, repositories, and logs.

Risk: External dependencies and live deployment behavior were not audited.

Mitigation: Review the companion skill and generated UI code, prefer reviewed package versions, and verify the relevant flows in the target application.

## Reference(s):

- [Managed Better Auth implementation](references/managed-auth.md)
- [Managed Better Auth as the OAuth server](references/oauth-server.md)
- [Self-managed Better Auth](references/self-managed.md)
- [Neon Auth overview](https://neon.com/docs/auth/overview.md)
- [Neon Auth production checklist](https://neon.com/docs/auth/production-checklist.md)
- [OAuth Provider plugin guide](https://neon.com/docs/auth/guides/plugins/oauth-provider.md)
- [Supabase Auth migration guide](https://neon.com/docs/auth/migrate/from-supabase.md)
- [Parent Neon skill](https://neon.com/docs/ai/skills/neon/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Framework-specific authentication setup guidance and verification steps.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
