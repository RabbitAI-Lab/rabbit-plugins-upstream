## Description:

Scaffold or extend an opinionated Next.js App Router fullstack application with TypeScript, NextAuth, Prisma, Route Handlers, RTK Query, Tailwind, shadcn/ui, React Hook Form, and Zod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to create new Next.js App Router projects or add feature/API slices using a consistent fullstack architecture. It is most useful when a project should route browser data through RTK Query to in-app Route Handlers backed by NextAuth, Prisma, and PostgreSQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create many files and install npm packages as part of a full Next.js scaffold.

Mitigation: Review the planned file list, package set, and generated diffs before allowing installation or writes in an existing workspace.

Risk: The skill can configure authentication, environment variables, and CI settings that affect application security.

Mitigation: Confirm selected auth providers, keep real secrets out of committed files, and review CI environment variables before deployment.

Risk: The skill can run Prisma, Docker, and database migration commands against the configured database.

Mitigation: Confirm the target DATABASE_URL and database host before migrations, prefer a local or development database first, and avoid destructive reset commands unless explicitly approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/nextjs-app-router)
- [Canonical Folder Layout](references/folder-layout.md)
- [Good Patterns to Keep](references/good-patterns.md)
- [Anti-patterns to Eliminate](references/anti-patterns.md)
- [NextAuth Configuration Template](references/templates/nextauth-config.md)
- [Prisma Schema Template](references/templates/prisma-schema.md)
- [Route Handler Template](references/templates/route-handler.md)
- [Feature Slice Template](references/templates/feature-slice.md)
- [Base RTK Query API Template](references/templates/api-base.md)
- [Testing Setup Template](references/templates/testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose broad project file creation, dependency installation, auth setup, CI setup, and database commands after user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
