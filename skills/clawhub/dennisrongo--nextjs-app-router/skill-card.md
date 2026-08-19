## Description:

Scaffolds and extends full-stack Next.js App Router applications with TypeScript, NextAuth v5, Prisma/PostgreSQL, Route Handlers, RTK Query, Tailwind, shadcn/ui, React Hook Form, and Zod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create production-oriented Next.js App Router projects or add feature and API slices that follow a consistent client-page, Route Handler, Prisma, NextAuth, RTK Query, and Zod architecture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional seed template can create a hardcoded admin test login.

Mitigation: Review or change seed credentials before use, keep seeding limited to local or test environments, and never seed production.

Risk: The skill may make broad project changes, install dependencies, run Prisma migrations, and query package or documentation sources.

Mitigation: Confirm database connection details, authentication providers, package versions, and migration targets before execution; review generated files and scanner results before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/nextjs-app-router)
- [Canonical Folder Layout](references/folder-layout.md)
- [Good Patterns to Keep](references/good-patterns.md)
- [Anti-patterns to Eliminate](references/anti-patterns.md)
- [NextAuth Config Template](references/templates/nextauth-config.md)
- [Prisma Schema Template](references/templates/prisma-schema.md)
- [Route Handler Template](references/templates/route-handler.md)
- [Package Template](references/templates/package.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write many project files, install packages, run Prisma generation and migrations, and request package or documentation lookups after user confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
