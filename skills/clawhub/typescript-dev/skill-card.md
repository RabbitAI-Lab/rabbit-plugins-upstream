## Description:

Builds full-stack TypeScript apps with Vite 8, React 19, Tailwind CSS v4, shadcn/ui, Biome, Vitest, and Hono.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when setting up or maintaining TypeScript projects that combine Vite, React, Tailwind CSS, shadcn/ui, Biome, Vitest, and Hono. It provides stack guidance, code and configuration examples, shell commands, testing guidance, and integration rules for type-safe frontend and backend development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-proposed commands or file edits could overwrite project files or change deployed services.

Mitigation: Review commands before execution, especially shadcn component overwrites, Biome --unsafe fixes, registry additions, MCP setup, and Wrangler deployment.

## Reference(s):

- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/typescript-dev)
- [Vite 8 reference](references/vite.md)
- [React 19 reference](references/react.md)
- [TypeScript 6.0 reference](references/typescript.md)
- [Tailwind CSS v4 reference](references/tailwind.md)
- [shadcn/ui reference](references/shadcn.md)
- [Biome reference](references/biome.md)
- [Vitest reference](references/vitest.md)
- [Hono reference](references/hono.md)
- [Vite documentation](https://vite.dev/guide/)
- [React Compiler documentation](https://react.dev/learn/react-compiler)
- [Tailwind CSS documentation](https://tailwindcss.com/docs)
- [shadcn/ui documentation](https://ui.shadcn.com/docs)
- [Hono documentation](https://hono.dev/docs/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline TypeScript, JSON, CSS, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; the agent may propose file edits, local tool commands, and deployment commands for review before execution.]

## Skill Version(s):

0.3.4 (source: frontmatter, changelog released 2026-08-21, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
